
disp('Hello');

[allframedata, map] = imread('An_MRI-Compatible_Robotic_System_for_Breast_Biopsy.gif', 'frames', 'all'); 
alldimensions = size(allframedata); 
number_of_frames = alldimensions(end);

for i=1:number_of_frames
im = allframedata(:,:,1,i);
frame_index = num2str(i);

imshow(im, map)
disp(i)

end