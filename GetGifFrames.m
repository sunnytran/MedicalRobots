% Get images from gif and save then to the folder
[allframedata, map] = imread('An_MRI-Compatible_Robotic_System_for_Breast_Biopsy.gif', 'frames', 'all'); 
alldimensions = size(allframedata); 
number_of_frames = alldimensions(end);
for i=1:number_of_frames
im = allframedata(:,:,1,i);
num = num2str(i);
% Tell your image names in first ''
nombre = strcat('im',num,'.jpg');
imwrite(im,map,nombre)
end