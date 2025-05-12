# HeartGuard-ECG-Image-Analysis-for-Cardiovascular-Anomaly-Detection

Cardiovascular diseases (CVDs) are coronary diseases that hamper the functioning of the circulatory system, particularly the heart, causing overall damage to the body of an individual. These diseases include myocardial infarction, arrhythmia, abnormal heartbeat, among others. CVDs have been recognized as the world’s leading cause of death by the World Health Organization. What makes these diseases even more lethal is the rate at which they progress, which is usually fast as compared to other abnormalities. They often progress silently and, if not diagnosed timely, can lead to death. Therefore, timely diagnosis and treatment of CVDs is crucial in the medical domain.

One of the main tools used for tracing cardiac activity is the ECG, which is recorded on paper. ECGs are recorded using waveforms that represent electrical activity of the heart over instances of time. This electrical activity of the heart is the result of action potential modeled as time-varying signals. Traditional ECG interpretation and analysis are heavily dependent on manual interpretation by healthcare professionals and doctors, making this process time-consuming and error-prone. Also, it is limited by the availability of trained professionals in this field.

**HeartGuard** aims to counter these challenges by using different approaches for image analysis and signal extraction, and by using data in various forms to train intelligent ML/DL architectures capable of predicting the correct class of cardiovascular anomaly. Its capacity to expedite the process of diagnosis and lessen the dependency on human interpretation makes it useful for all medical settings, from big hospitals to small clinics lacking diagnostic tools and facilities.

The architecture and working of HeartGuard are defined in the PDF file called `Documentation.pdf`, and all the necessary code is available in the repository. The path file of the VGG16 model (best model) is shared above and can be used locally for deployment.

HeartGuard is currently deployed using **Gradio** (Google Colab). We aim to shift it to a permanent deployment platform like **HuggingFace** for future use in medical settings.

---

## 🚀 Installation and Usage

Follow the steps below to set up the environment and run **HeartGuard**:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/HeartGuard-ECG-Image-Analysis-for-Cariovascular-Anomaly-Detection.git
cd HeartGuard-ECG-Image-Analysis-for-Cardiovascular-Anomaly-Detection
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)

It’s recommended to use a virtual environment. You can create and activate one as follows:

```bash
conda create -n heartguard-env python=3.8
conda activate heartguard-env
```

### 3. Install the Dependencies

Install all the required dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📁 Folder Structure

Ensure your ECG images are properly formatted and placed in the correct directories. The expected folder structure is as follows:

```bash
HeartGuard-ECG-Image-Analysis-for-Cardiovascular-Anomaly-Detection/
├── dataset/
│   ├── Image Preprocessing for 1D data/
│   └── Processing Images for DL models/
```

---

## ⚙️ Usage

### 1. Prepare the Data

Place your preprocessed ECG images in the appropriate folders as shown above.

### 2. Train the Model

Run the training script to begin training:

```bash
jupyter notebook DL-models/Resnet/Resnet_uncropped.ipynb
```

### 3. Deploy the Model

Edit the Python code to adjust the path for the saved model, then run the code. A Gradio link will be generated for interactive use.

---

## 🧠 Notes

* Make sure your data is clean and properly labeled.
* Gradio is used for the deployment and demonstration of predictions.

---

