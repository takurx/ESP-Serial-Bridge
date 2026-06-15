import argparse
import os
import struct
import time
import binascii

import serial

MAGIC = b"SB"
HEADER_FORMAT = "<2sIH"  # magic(2), seq(uint32), payload_len(uint16)
CRC_FORMAT = "<H"        # crc16(uint16)


def crc16_ccitt(data: bytes) -> int:
    return binascii.crc_hqx(data, 0xFFFF)


def build_frame(seq: int, payload: bytes) -> bytes:
    header = struct.pack(HEADER_FORMAT, MAGIC, seq, len(payload))
    crc = crc16_ccitt(header + payload)
    return header + payload + struct.pack(CRC_FORMAT, crc)


def main() -> None:
    parser = argparse.ArgumentParser(description="Send framed serial packets with sequence + CRC16")
    parser.add_argument("--port", default="COM18", help="Serial port (example: COM18)")
    parser.add_argument("--baud", type=int, default=115200, help="Baud rate")
    parser.add_argument("--payload", type=int, default=256, help="Payload bytes per frame")
    parser.add_argument("--report-interval", type=float, default=1.0, help="Seconds between reports")
    parser.add_argument("--duration", type=float, default=0.0, help="Run time in seconds (0 = infinite)")
    args = parser.parse_args()

    if args.payload <= 0 or args.payload > 65535:
        raise ValueError("--payload must be in range 1..65535")
    if args.report_interval <= 0:
        raise ValueError("--report-interval must be > 0")

    seq = 0
    frame_bytes_sent = 0
    payload_bytes_sent = 0

    start_total = time.perf_counter()
    start_window = start_total

    with serial.Serial(args.port, args.baud, timeout=0) as ser:
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        while True:
            payload = os.urandom(args.payload)
            frame = build_frame(seq, payload)

            written = ser.write(frame)
            frame_bytes_sent += written
            payload_bytes_sent += len(payload)
            seq = (seq + 1) & 0xFFFFFFFF

            now = time.perf_counter()
            window_elapsed = now - start_window
            total_elapsed = now - start_total

            if window_elapsed >= args.report_interval:
                frame_bps = (frame_bytes_sent / window_elapsed) * 10.0
                payload_bps = (payload_bytes_sent / window_elapsed) * 8.0
                print(
                    f"TX frame_bps(8N1)={frame_bps:,.0f} "
                    f"payload_bps={payload_bps:,.0f} "
                    f"frames={seq:,}"
                )
                frame_bytes_sent = 0
                payload_bytes_sent = 0
                start_window = now

            if args.duration > 0 and total_elapsed >= args.duration:
                break


if __name__ == "__main__":
    main()
