# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from enum import IntEnum
from typing import List, Optional
from xdrlib import Packer, Unpacker

from ..__version__ import __issues__
from ..exceptions import ValueError
from .base import (
    Boolean,
    Hyper,
    Integer,
    Opaque,
    String,
    UnsignedHyper,
    UnsignedInteger,
)
from .constants import *

__all__ = ["RevokeSponsorshipType"]


class RevokeSponsorshipType(IntEnum):
    """
    XDR Source Code
    ----------------------------------------------------------------
    enum RevokeSponsorshipType
    {
        REVOKE_SPONSORSHIP_LEDGER_ENTRY = 0,
        REVOKE_SPONSORSHIP_SIGNER = 1
    };
    ----------------------------------------------------------------
    """

    REVOKE_SPONSORSHIP_LEDGER_ENTRY = 0
    REVOKE_SPONSORSHIP_SIGNER = 1

    def pack(self, packer: Packer) -> None:
        packer.pack_int(self.value)

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "RevokeSponsorshipType":
        value = unpacker.unpack_int()
        return cls(value)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "RevokeSponsorshipType":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "RevokeSponsorshipType":
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)

    @classmethod
    def _missing_(cls, value):
        raise ValueError(
            f"{value} is not a valid {cls.__name__}, please upgrade the SDK or submit an issue here: {__issues__}."
        )
