<h1>Iris detection and Glare Mitigation utilizing Inpainting Mechanism<h1>
  
<h4>What is iris detection?</h4>
<p>Iris detection in biometrics refers to the process of capturing and identifying the unique 
patterns found in the iris of the human eye for the purpose of authentication and 
identification. The iris is the colored part of the eye that surrounds the pupil, and it is known 
for its intricate and highly distinctive patterns, which can be used to distinguish one 
individual from another.</p>

<h4>Application of Iris detection</h4>
<li> Biometric Security</li>
<li> Border Control and Immigration</li>
<li> Healthcare Patient Identification</li>
<li> Financial Transactions and Banking</li>

<h4>Advantages of iris as biometric over other biometric data</h4>
<li> No physical contact is required</li>
<li> Less prone to damage</li>
<li> Age invariant</li>
<li> Has higher accuracy and reliability than other biometrics such as fingerprint</li>

<h4>Major issues with current iris recognition systems</h4>
<li><b>Cost of equipment</b>: Specialized hardware and cameras are often required for iris 
recognition, making the deployment of such systems more costly and less accessible for 
some applications</li>
<li><b>Constrained image capture conditions</b>: Glare and reflections can reduce the overall 
quality of iris images by causing overexposure or brightness variations. These issues can 
make it difficult to distinguish the fine details of the iris patterns. It can also increase the 
number of false rejections. Hence images are taken in very constrained environments
</li>

<h4>Current Solutions</h4>
<p>
  Many of the iris recognition systems currently use NIR illumination instead of visible light to 
reduce the likelihood of glare. NIR light is invisible to the human eye and is less likely to 
cause reflections and glare on the cornea.
While Near-Infrared (NIR) illumination offers several advantages for iris detection, it also 
comes with certain disadvantages and challenges. Here are some major drawbacks 
associated with using NIR illumination in iris detection:
</p>
<br>
<li><b>Cost</b>: NIR imaging systems, including cameras and light sources, can be more 
expensive than their visible counterparts. This may contribute to higher overall 
system costs.
</li>
<br>
<li><b>Complexity</b>: NIR imaging systems often require more sophisticated hardware, 
including specialized light sources and sensors. The complexity of these components 
can increase the overall complexity of the system</li>
<br>
<li><b>Eye Safety Concerns</b>: While NIR light is generally considered safe for imaging 
applications, there may be concerns related to eye safety, especially in continuous 
exposure situations. Proper safety measures must be implemented to ensure no 
harm to the eyes of individuals being scanned.</li>
<br>
<li><b>Reduced Color Information</b>: NIR imaging typically captures grayscale or 
monochromatic images, limiting the color information available compared to RGB 
imaging. In applications where color information is important, additional 
considerations may be needed.</li>
<br>
<li><b>Bulkiness of Equipment</b>: NIR cameras and associated equipment may be bulkier 
compared to visible light cameras, which could be a concern in applications where 
compactness is essential.</li>

<p align="center"><img src="Photos/Screenshot 2023-12-15 052517.png" alt="Iris detection system"></p>
<p align="center"><img src="Photos/Screenshot 2023-12-15 053133.png" alt="Samsung iris detection"></p>
<p align="center"><b>Samsung Iris Detection System</b></p>

<H3>My Solution and Results</H3>
<p>The majority of the above-mentioned disadvantages of NIR images can be dealt with just by 
using RGB (visible light spectrum) images. However, the major problem with images in the 
visible spectrum is the glare and reflection present in the iris images.</p>
<p>Hence, I propose a novel inpainting-based eye-glare removal mechanism</p>

<h4>Eye Glare Mitigation Through Inpainting-Based Mechanism</h4>
<p>Inpainting is a technique used in image processing to fill in or restore damaged or missing 
parts of an image. The goal of inpainting is to create a visually plausible completion of the 
damaged or missing regions based on the information available in the surrounding areas of 
the image.</p>

<p>Many inpainting methods have been developed over the years with recent approaches 
made to deep inpainting (deep-learning-based inpainting). However, over here we constrain
ourselves to the more traditional but effective inpainting methods namely the Navier-Stoke 
method.</p>

<p>which uses the Navier-Stoke equation from fluid dynamics to model the propagation of the 
inpainting by getting a direct solution for the Navier-Stoke equation along the Isophotes of 
the generated contours
</p>
<b>I have further shared the results of my implementation below.</b>

<p align="center"><img src="Photos/Screenshot 2023-12-15 053932.png" alt="Navier-Stokes Equation"></p>

<h4>Proposed Algorithm</h4>
<ol>
  <li><b>Resize</b>: All incoming images are resized to a constant shape for easier filtering of 
contours</li>
  <li><b>Thresholding</b>: Binarizing the image by first converting to grayscale and then 
thresholding</li>
  <li><b>Find contours</b>: Get the contours in the binarized image</li>
  <li><b>Filter contours</b>: Remove all contours above a certain area threshold</li>
  <li><b>Generate mask</b>: Transfer the filtered contours to a new mask</li>
  <li><b>Inpainting</b>: Pass the generated mask to the inpainting function along with a suitable 
radius.</li>
</ol>

<p align="center"><img src="Photos/Screenshot 2023-11-11 003306.png" alt"Inpainting Glare Removal Mechanism"></p>
<p align="center"><b>Algorithm Flow</b></p>

<p align="center"><img src="Photos/Screenshot 2023-12-15 054754.png" alt"Results"></p>
<p align="center"><img src="Photos/Screenshot 2023-12-15 054858.png" alt"Results"></p>

<h4>Iris Segmentation</h4>
<ol>
  <li><b>Grayscale</b>: Convert the image to grayscale</li>
  <li><b>Denoising</b>: Performing gaussian blur</li>
  <li><b>Edge detection</b>: Detect the edges using Canny</li>
  <li><b>Hough Circles</b>: Get the circles in the image using the Hough circle</li>
  <li><b>Mask</b>: Generate a mask based on the circle locations</li>
  <li><b>Thresholding</b>: Remove unnecessary segments in the masked image using 
thresholding</li>
</ol>

<p align="center"><img src="Photos/Screenshot 2023-12-15 054933.png" alt="Iris segmentation"></p>
<br>
<p align="center"><img src="Photos/Screenshot 2023-12-15 054957.png" alt="Segmentation results"></p>

<h4>Overall inpainting offers the following advantages to the task of Iris detection</h4>

<ol>
  <li> Allowing for the use of RGB images for iris biometric matching</li>
  <li> Glare and Reflection Removal</li>
  <li> Better segmentation result </li>
  <li> Improved Iris texture extraction</li>
</ol>
