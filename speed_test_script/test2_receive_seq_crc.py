import argparse
import struct
import time
import binascii

import serial

MAGIC = b"SB"
HEADER_FORMAT = "<2sIH"  # magic(2), seq(uint32), payload_len(uint16)
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
CRC_FORMAT = "<H"
CRC_SIZE = struct.calcsize(CRC_FORMAT)
MAX_PAYLOAD = 4096


def crc16_ccitt(data: bytes) -> int:
    return binascii.crc_hqx(data, 0xFFFF)


def main() -> None:
    parser = argparse.ArgumentParser(description="Receive framed serial packets and measure throughput/loss")
    parser.add_argument("--port", default="COM29", help="Serial port (example: COM29)")
    parser.add_argument("--baud", type=int, default=115200, help="Baud rate")
    parser.add_argument("--report-interval", type=float, default=1.0, help="Seconds between reports")
    parser.add_argument("--duration", type=float, default=0.0, help="Run time in seconds (0 = infinite)")
    parser.add_argument("--read-chunk", type=int, default=4096, help="Serial read size per loop")
    args = parser.parse_args()

    if args.report_interval <= 0:
        raise ValueError("--report-interval must be > 0")
    if args.read_chunk <= 0:
        raise ValueError("--read-chunk must be > 0")

    buf = bytearray()
    last_seq = None

    ok_frames = 0
    crc_error_frames = 0
    lost_frames = 0
    payload_bytes_ok = 0
    frame_bytes_ok = 0

    start_total = time.perf_counter()
    start_window = start_total

    with serial.Serial(args.port, args.baud, timeout=0.05) as ser:
        ser.reset_input_buffer()

        while True:
            chunk = ser.read(args.read_chunk)
            if chunk:
                buf.extend(chunk)

            # Parse as many complete frames as possible.
            while True:
                if len(buf) < HEADER_SIZE + CRC_SIZE:
                    break

                if buf[0:2] != MAGIC:
                    idx = buf.find(MAGIC, 1)
                    if idx == -1:
                        del buf[:-1]
                    else:
                        del buf[:idx]
                    continue

                _, seq, payload_len = struct.unpack_from(HEADER_FORMAT, buf, 0)
                if payload_len > MAX_PAYLOAD:
                    del buf[0:1]
                    continue

                frame_len = HEADER_SIZE + payload_len + CRC_SIZE
                if len(buf) < frame_len:
                    break

                frame = bytes(buf[:frame_len])
                recv_crc = struct.unpack_from(CRC_FORMAT, frame, frame_len - CRC_SIZE)[0]
                calc_crc = crc16_ccitt(frame[:-CRC_SIZE])

                if recv_crc != calc_crc:
                    crc_error_frames += 1
                    del buf[0:2]
                    continue

                payload = frame[HEADER_SIZE:HEADER_SIZE + payload_len]
                _ = payload  # payload data itself is intentionally ignored in this benchmark

                if last_seq is not None:
                    gap = (seq - last_seq - 1) & 0xFFFFFFFF
                    lost_frames += gap
                last_seq = seq

                ok_frames += 1
                payload_bytes_ok += payload_len
                frame_bytes_ok += frame_len

                del buf[:frame_len]

            now = time.perf_counter()
            window_elapsed = now - start_window
            total_elapsed = now - start_total

            if window_elapsed >= args.report_interval:
                frame_bps = (frame_bytes_ok / window_elapsed) * 10.0
                payload_bps = (payload_bytes_ok / window_elapsed) * 8.0
                total_seen = ok_frames + crc_error_frames + lost_frames
                loss_ratio = (lost_frames / total_seen) * 100.0 if total_seen > 0 else 0.0

                print(
                    f"RX frame_bps(8N1)={frame_bps:,.0f} "
                    f"payload_bps={payload_bps:,.0f} "
                    f"ok={ok_frames:,} crc_err={crc_error_frames:,} "
                    f"lost={lost_frames:,} loss={loss_ratio:.3f}%"
                )

                ok_frames = 0
                crc_error_frames = 0
                lost_frames = 0
                payload_bytes_ok = 0
                frame_bytes_ok = 0
                start_window = now

            if args.duration > 0 and total_elapsed >= args.duration:
                break


if __name__ == "__main__":
    main()
