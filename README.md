# Recognition of Anomaly in the retina using OCT B scans 
This project consists of two major parts :
1) Training the module that generates maps for the detection of lesions in the retina.
   This helps achieve:
   1) Better classification accuracy as the regions with lesions in the attention map are given more importance and the rest of the regions are suppressed.
   2) Better understanding of how the model is performing as this is the way naturally that opthamologists use to detect the presence of anomalies and their type.
2) Training the CNN that uses feature maps from the module that generetes attention maps and the feature maps   
