#!/usr/bin/env python3
import time

from hexdump import hexdump

from panda import Panda
from panda.python.isotp import isotp_recv, isotp_send


if __name__ == "__main__":
  BUS = 0
  ECU_ADDR = 0x24b
  ADDR_OFFSET = 0x400
  EXT_DIAG_REQUEST = b"\x10\x03"
  COM_CONT_REQUEST = b"\x28"
  TESTER_REQUEST = b"\x3E"


  panda = Panda()
  panda.set_safety_mode(Panda.SAFETY_ELM327)

  isotp_send(panda, EXT_DIAG_REQUEST, ECU_ADDR, bus=BUS)
  hexdump(isotp_recv(panda, ECU_ADDR + ADDR_OFFSET, bus=BUS))

  isotp_send(panda, TESTER_REQUEST, ECU_ADDR, bus=BUS)
  hexdump(isotp_recv(panda, ECU_ADDR + ADDR_OFFSET, bus=BUS))

  isotp_send(panda, COM_CONT_REQUEST, ECU_ADDR, bus=BUS)
  hexdump(isotp_recv(panda, ECU_ADDR + ADDR_OFFSET, bus=BUS))
  hexdump(isotp_recv(panda, ECU_ADDR + ADDR_OFFSET, bus=BUS))