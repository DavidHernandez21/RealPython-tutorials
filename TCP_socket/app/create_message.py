import sys
import struct

import encoding_decoding


def new_message(*, content_bytes: bytes, content_type: str, content_encoding: str):

    jsonheader = {
        "byteorder": sys.byteorder,
        "content-type": content_type,
        "content-encoding": content_encoding,
        "content-length": len(content_bytes),
    }

    jsonheader_bytes = encoding_decoding.json_encode(jsonheader, "utf-8")
    message_hdr = struct.pack(">H", len(jsonheader_bytes))
    message = message_hdr + jsonheader_bytes + content_bytes
    return message