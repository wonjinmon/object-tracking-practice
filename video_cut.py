import cv2


video_path = "./sample_video.mp4"
save_path = "./output"

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)

frame_count = 0
while cap.isOpened():
    retval, image = cap.read()  # retval: T or F, image: frame(np.ndarray)
    frame_count += 1
    if retval:
        cv2.imshow("image", image)
        key = cv2.waitKey()

        if key == 32:  # 스페이스바를 누르면 저장 시작
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            out = cv2.VideoWriter(
                f"{save_path}/clip_{frame_count}.mp4",
                fourcc,
                30,
                (image.shape[1], image.shape[0]),
            )
            i = 0
            while cap.isOpened():
                i += 1
                retval, image = cap.read()
                if key == 13:  # 엔터키를 누르면 종료
                    break
                if i == 100:  # 100 frame 도달시 종료
                    break
                if retval:
                    out.write(image)
                    cv2.imshow("image", image)
                    key = cv2.waitKey(25)
            out.release()
            cv2.destroyAllWindows()
    cap.release()

print("")  # 100 프레임까지 저장되었는지 확인

file = "./output/clip_1.mp4"
video = cv2.VideoCapture(file)

total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(total_frames)
