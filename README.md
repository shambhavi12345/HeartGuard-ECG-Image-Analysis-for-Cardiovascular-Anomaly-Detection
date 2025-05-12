# HeartGuard-ECG-Image-Analysis-for-Cardiovascular-Anomaly-Detection
Cardiovascular diseases (CVDs) are coronary diseases that hamper the functioning of the circulatory system, particularly the heart, causing overall damage to the body of an individual. These diseases include myocardial infraction, arrhythmia, abnormal heartbeat, among others. CVDs have been recognised as the world’s leading cause of death by the World Health Organisation. What makes these diseases even more lethal is the rate at which they progress, which is usually fast as compared to other abnormalities. The often progress silently and if not diagnosed timely, can lead to death. Therefore, timely diagnosis and treatment of CVDs is crucial in the medical domain. 

One of the main tools used for tracing cardiac activity is the ECG which is recorded on paper. ECGs are recorded using waveforms that represent electrical activity of the heart over instances of time. This electrical activity of the heart is the result of action potential modelled as time-varying signals. Traditional ECG interpretation and analysis is heavily defendant on manual interpretation by healthcare professionals and doctors, making this process time-consuming an error-prone. Also, it is limited by the availability of trained professionals in thi field. 

HeartGuard aims to counter these challenges by using different approaches for image analysis and signal extraction and using data in different forms for training intelligent ML/DL architectures, capable of predicting the correct class of cardiovascular anomaly. Its capacity to expedite the process of diagnosis and lessen the dependency on human interpretation makes it useful for all medical settings engaging from big hospitals to even small clinics with lack of diagnostic tools and facilities. 

The architecture and working of HeartGuard is defined in the PDF file called "Documentation.pdf" and all the necessary codes are given in the repo itself. Also, the path file of the VGG16 model(best model) is shared above and can be used locally for deployment. 

HeartGuard is currently deployed using Gradio(Google Colab). We aim to shift it to permanent deployment platform like HuggingFace for future use in medical settings. 


🚀 Installation and Usage
Follow the steps below to set up the environment and run HeartGuard:

1. Clone the Repository
```bash
git clone https://github.com/your-username/HeartGuard-ECG-Image-Analysis-for-Cariovascular-Anomaly-Detection.git
cd HeartGuard-ECG-Image-Analysis-for-Cardiovascular-Anomaly-Detection

3. Create and Activate a Virtual Environment (Optional but Recommended)
```bash
conda create -n heartguard-env python=3.8
conda activate heartguard-env

4. Install the Dependencies
```bash
pip install -r requirements.txt
📁 Folder Structure
Ensure your ECG images are properly formatted and placed in the correct directories. The expected structure is:
```bash
HeartGuard-ECG-Image-Analysis-for-Cariovascular-Anomaly-Detection/
├── dataset/
│   ├── Image Preprocessing for 1D data/
│   └── Processing Images for DL models/


⚙️ Usage
1. Prepare the Data
Place your preprocessed ECG images in the appropriate folders as shown above.

2. Train the Model
Run the training script to begin training:
```bash
jupyter notebook DL-models/Resnet/Resnet_uncropped.ipynb

3. Deploy the Model
Edit the Python code to adjust the path for the saved model, then run the code. A Gradio link will be generated for interactive use.



🧠 Notes
Make sure your data is clean and properly labeled.
Gradio is used for the deployment and demonstration of predictions.






