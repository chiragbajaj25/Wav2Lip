def img_vid(imgs):
    import cv2
    for x in imgs: # Change the range according to your requirement
        path = f"/content/gdrive/MyDrive/NFT_Art/Images/image{x}.jpg"
        path_out = f"/content/gdrive/MyDrive/NFT_Art/input_videos/image{x}.mp4"
        img = cv2.imread(path)
        framearray = []
        for x in range(1, 24*27):
            framearray.append(img)
        out = cv2.VideoWriter(path_out, cv2.VideoWriter_fourcc(*'DIVX'), 24, (img.shape[0], img.shape[1]))
        for i in range(len(framearray)):
            out.write(framearray[i])
        out.release()