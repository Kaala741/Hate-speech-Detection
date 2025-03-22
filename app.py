import streamlit as st
from preprocessing import preprocess_text
from model import load_model,predict
from streamlit_lottie import st_lottie
import requests
import tempfile
import os
from graphviz import Digraph

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return new_func()
    return r.json()

# Load the model and tokenizer
model_path = 'bert_classifier.h5'
model, tokenizer = load_model(model_path)

lottie_coding = load_lottieurl("https://lottie.host/05d8286a-86bb-483e-a845-5715aca4241e/hrUyVR89oh.json")
lottie_coding2 = load_lottieurl("https://lottie.host/5735c629-79f5-4312-b4e4-268709e0eaab/D4OjpsayFs.json")

# Streamlit UI
st.set_page_config(layout="wide",page_title="Hate-speech-Detection",page_icon=":computer:")
st.markdown("<h1 style='text-align:center;color:white;'>Welcome To Our Website !</h1>", unsafe_allow_html=True)
#---Main Section---
with st.container():
    st.header(':Automated Hate Speech Detection')
    input_text = st.text_area('Enter text to analyze', '')
    if st.button('Analyze'):
         preprocessed_text = preprocess_text(input_text)
         classification = predict(preprocessed_text, model, tokenizer)
         st.write("Classification:", classification)
st.write("---")
#---Header Section---
with st.container():
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("ABOUT US")
        st.write(
    """
    This website employs an automated system to detect and manage harmful content that incites hatred, violence, or discrimination against individuals or groups based on characteristics such as race, ethnicity, gender, sexual orientation, or religion. By using machine learning algorithms and natural language processing, the system analyzes user-generated comments and posts on the Reddit platform to identify and flag potentially offensive or harmful language
    """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")
st.write("---")       
#---architecture section---
with st.container():
   st.title("Project Architecture")
   # Path to the architecture image
   architecture_image = "Screenshot 2025-03-20 231143.png"  # Replace with the path to your image

   # Display the architecture image
   st.image(architecture_image, caption="Project Architecture Diagram", use_column_width=True)
st.write("---")
#Resources section
with st.container():
   st.title("Resources")
# Introduction
   st.write("""
Welcome to the Resources page! Here, you'll find helpful links, articles, and tools related to hate speech detection and online safety.
""")

# Section 1: Articles and Research Papers
   st.header("Articles and Research Papers")
   st.write("""
Here are some articles and research papers on hate speech detection:
- [Hate Speech Detection: Challenges and Solutions](https://pmc.ncbi.nlm.nih.gov/articles/PMC6701757/)
- [Machine Learning Approaches for Hate Speech Classification](https://www.geeksforgeeks.org/hate-speech-detection-using-deep-learning/)
- [The Impact of Hate Speech on Social Media](https://crimesciencejournal.biomedcentral.com/articles/10.1186/s40163-024-00204-y)
""")

# Section 2: Tools and Libraries
   st.header("Tools and Libraries")
   st.write("""
Here are some tools and libraries you can use for hate speech detection:
- **Python Libraries:**
  - [Natural Language Toolkit (NLTK)](https://www.nltk.org/)
  - [spaCy](https://spacy.io/)
  - [Hugging Face Transformers](https://huggingface.co/transformers/)
- **Datasets:**
  - [Hate speech Dataset on GitHub](https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech)
  - [Hate Speech Dataset on Kaggle](https://www.kaggle.com/datasets)
  - [Hatebase](https://hatebase.org/)
""")

# Section 3: Online Courses and Tutorials
   st.header("Online Courses and Tutorials")
   st.write("""
Here are some online courses and tutorials to learn more about hate speech detection:
- [Coursera: Natural Language Processing](https://www.coursera.org/)
- [Udemy: Machine Learning for Text Data](https://www.udemy.com/)
- [YouTube: Hate Speech Detection Tutorial](https://www.youtube.com/)
""")

# Section 4: Organizations and Initiatives
   st.header("Organizations and Initiatives")
   st.write("""
Here are some organizations working to combat hate speech:
- [Anti-Defamation League (ADL)](https://www.adl.org/)
- [Southern Poverty Law Center (SPLC)](https://www.splcenter.org/)
- [UNESCO: Countering Online Hate Speech](https://en.unesco.org/)
""")

# Section 5: Report Hate Speech
   st.header("Report Hate Speech")
   st.write("""
If you encounter hate speech online, here's how you can report it:
- **Facebook:** [Report Hate Speech](https://www.facebook.com/help/)
- **Twitter:** [Report Hateful Conduct](https://help.twitter.com/en/safety-and-security/report-abusive-behavior)
- **Instagram:** [Report Hate Speech](https://help.instagram.com/contact/606967319425038)
""")
with st.expander("Privacy Policy"):
    st.write("""
    **Privacy Policy**

    We are committed to protecting your privacy. This Privacy Policy explains how we collect, use, and safeguard your information when you use our website.

    1. **Information We Collect:**
       - Data from social media platforms (e.g., tweets, comments, posts) that you provide for analysis.
       - Metadata related to your usage of our services.

    2. **How We Use Your Information:**
       - To analyze social media content for hate speech detection.
       - To improve the accuracy and performance of our hate speech detection algorithms.
       - To provide you with insights and reports based on the analyzed data.

    3. **Data Security:**
       - We use industry-standard security measures to protect your data.
       - All data is processed securely and is not stored longer than necessary.

    4. **Third-Party Services:**
       - We may use third-party APIs or services to access social media data, but we do not share your personal information without your consent.

    5. **Your Rights:**
       - You have the right to request access to, correction, or deletion of your data.
       - You can opt out of data collection at any time.

    """)
with st.expander("Community Guidelines"):
    st.write("""
    **1. Be Respectful:**
       - Treat all users with respect and kindness.
       - Do not engage in hate speech, harassment, or bullying.

    **2. No Harmful Content:**
       - Do not upload or analyze content that promotes violence, discrimination, or illegal activities.
       - Ensure that the data you provide complies with the terms of the social media platforms it comes from.

    **3. Protect Privacy:**
       - Do not share personal information about yourself or others.
       - Ensure that any data you provide for analysis does not violate the privacy rights of others.

    **4. Follow the Law:**
       - Do not use our platform for illegal activities or to violate the rights of others.
       - Comply with all applicable laws and regulations.

    **5. Report Violations:**
       - If you encounter any content or behavior that violates these guidelines, please report it to us immediately.
       - Use the reporting tools provided on our platform.

    **6. Be Honest:**
       - Do not impersonate others or provide false information.
       - Use our platform responsibly and ethically.

    **7. Consequences of Violations:**
       - Violations of these guidelines may result in the suspension or termination of your access to our platform.
       - Serious violations may be reported to the appropriate authorities.

    Thank you for helping us maintain a positive and inclusive community!
    """)
# Terms of Service
with st.expander("Terms of Service"):
    st.write("""
    **Terms of Service**

    By using our website, you agree to the following terms and conditions:

    1. **Acceptable Use:**
       - You agree not to upload or analyze harmful, illegal, or abusive content.
       - You are responsible for ensuring that you have the right to use and analyze the social media data you provide.

    2. **Data Collection from Social Media:**
       - By using our services, you grant us permission to access and analyze data from social media platforms as provided by you.
       - You must comply with the terms and policies of the social media platforms from which the data is collected.

    3. **Intellectual Property:**
       - All content and trademarks on this site are the property of their respective owners.
       - You retain ownership of the data you provide, but you grant us a license to use it for analysis purposes.

    4. **Limitation of Liability:**
       - We are not responsible for any damages arising from the use of our services or the accuracy of the hate speech detection results.

    5. **Changes to Terms:**
       - We reserve the right to modify these terms at any time. Continued use of our services constitutes acceptance of the updated terms.

    If you do not agree with these terms, please do not use our services.
    """)
# --- FORM SECTION ---
with st.container():
    st.write("---")
    st.header(":violet[CONTACT US !]")
    contact_form = """
    <form action="https://formsubmit.co/seelammanikanta777@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("form.css")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding2, height=300,key="anime")