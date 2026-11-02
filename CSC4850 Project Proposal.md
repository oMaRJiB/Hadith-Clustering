# CSC 4850 Project Proposal
*Team Members:*
Omar Jibreen ojibreen1@student.gsu.edu
## Project Title: Semantic Variation Clustering in Prophetic Hadiths

### Summary
> The traditions of the Prophet Muhammad, known as Hadith, has been preserved via oral transmission chains before compiled into text collections. Due to narrators sometimes relying on narrating by meaning, exact wording of single event often varies across volumes or chains of narrations.

>Traditional string matching and keyword searches fail when sentences use synonyms, reprashing, or entirely different vocabularies. For this reason, this project aims to use clustering and semantic similariy testing to group hadiths together based on underlying meaning, themes, and events.

> Techniques and algorithms that will be used include TF-IDF, and K-Means clustering. ARaBERT will be utilized to preprocess arabic text into features that will be fed into a clustering algorithm.

#### Datasets
> The primary dataset used will be the Ifta Sunnah Hadith Corpus on Kaggle or other similar dataset.

#### Action Plan
* Determine dataset; inspect and clean data
* Implement arabic text preprocesssing
* Implement K-means clustering
* Implement AraBERT
* Evaluate and compare clustering results using appropriate metrics and qualitative analysis of related narrations
Week 6: Analyze results, create visualizations, finalize the implementation, and prepare the project report and presentation

##### Resources
* Ifta Sunnah Hadith Corpus
* ARaBERT
* Scikit-learn documentation for TF-IDF and K-Means
* Hugging Face Transformer documentation and pretrained arabic language models