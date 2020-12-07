im= imread('testannot_rect/0099.png'); %rectangle annotation

[r, c] = find(im);
r1 = min(r);
r2 = max(r);
c1 = min(c);
c2 = max(c);


bb1 = [c1, r1, c2-c1, r2-r1];
bb2 = [132,113,41,68]; %levo/desno -> from image_ear_detection.py

over_lap = bboxOverlapRatio(bb1,bb2)*100; %return the percentage of the overlap/accuracy
over_lap 