import streamlit as st
from PIL import Image

from transformers import pipeline
import numpy as np
from transformers import AutoFeatureExtractor, AutoModelForImageClassification


st.set_page_config(layout='wide',
                   page_title='Recycleable Material Classification'
                   )


def main():
    
    st.title("Recycleable Material Classification")
    st.markdown("# Machine Learning Technique")  
    st.markdown("The model is based on the [ViT](https://huggingface.co/google/vit-base-patch16-224-in21k) model, which is short for the Vision Transformer. It was introduced in the paper [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929), which was introduced in June 2021 by a team of researchers at Google Brain. And first released in [this repository](https://github.com/rwightman/pytorch-image-models). I trained this model with PyTorch. I think the most different thing between using the transformer to train on an image and on a text is in the tokenizing step. ")  
    st.markdown("There are 3 steps to tokenize the image:")  
    st.markdown("1. Split an image into a grid of sub-image patches")  
    st.markdown("2. Embed each patch with a linear projection")  
    st.markdown("3. Each embedded patch becomes a token, and the resulting sequence of embedded patches is the sequence you pass to the model.")  
    vit=Image.open("pic/ViT.png")
    st.image(vit)
    st.markdown("The Transformer is trained with 30 epochs, with Adam as the optimization regime. The overall accuracy on the test set is roughly 95% with an AUC of 0.92.")
    st.markdown("## Resource Links")  
    st.markdown("[vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k)")  
    st.markdown("[Garbage dataset](https://huggingface.co/cardiffnlp/twitter-roberta-base)")  
    st.markdown("[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)")  
    st.header("Upload your .jpeg and try it out!")

    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'])
    
    if uploaded_file!=None:

        img=Image.open(uploaded_file)

        extractor = AutoFeatureExtractor.from_pretrained("hagerty7/recyclable-materials-classification")
        model = AutoModelForImageClassification.from_pretrained("hagerty7/recyclable-materials-classification")

        inputs = extractor(img,return_tensors="pt")
        outputs = model(**inputs)
        label_num=outputs.logits.softmax(1).argmax(1)
        label_num=label_num.item()
        st.write("The predicted class is:")
        if label_num==0:
            st.write("cardboard")
        elif label_num==1:
            st.write("glass")
        elif label_num==2:
            st.write("metal")
        elif label_num==3:
            st.write("paper")
        elif label_num==4:
            st.write("plastic")
        else:
            st.write("trash")

        st.image(img)



if __name__ == '__main__':
    main()