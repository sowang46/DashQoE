import asyncio
import logging
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer
from utils.signaling import TcpSocketSignaling

async def main():
    pc = RTCPeerConnection()

    # gather ICE candidates
    await pc.setLocalDescription(await pc.createOffer())

    # await collect_qoe(pc, player)

if __name__ == '__main__':
    asyncio.run(main())