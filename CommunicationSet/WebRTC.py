# # 설치: pip install aiortc
# import asyncio
# from aiortc import RTCPeerConnection, RTCSessionDescription
# from aiortc.contrib.signaling import BYE

# # 연결 기능
# async def webrtc_connect(offer_sdp, offer_type):
#     pc = RTCPeerConnection()
#     await pc.setRemoteDescription(RTCSessionDescription(sdp=offer_sdp, type=offer_type))
#     answer = await pc.createAnswer()
#     await pc.setLocalDescription(answer)
#     return pc, answer

# # 주는 기능
# async def webrtc_send(pc, channel_label, message):
#     channel = pc.createDataChannel(channel_label)
#     await channel.send(message)

# # 받는 기능
# async def webrtc_receive(pc, channel_label):
#     future = asyncio.Future()

#     @pc.on("datachannel")
#     def on_datachannel(channel):
#         @channel.on("message")
#         def on_message(message):
#             future.set_result(message)

#     return await future

# # 해제 기능
# async def webrtc_close(pc):
#     await pc.close()

# # Example usage
# # You need an offer SDP and type from another WebRTC peer to connect.
# offer_sdp = 'YOUR_OFFER_SDP'
# offer_type = 'offer'
# pc, answer = await webrtc_connect(offer_sdp, offer_type)
# await webrtc_send(pc, 'myChannel', 'Hello, WebRTC')
# print(await webrtc_receive(pc, 'myChannel'))
# await webrtc_close(pc)
