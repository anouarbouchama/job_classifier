import spacy

def job_classifier(text_to_classify,model):

    nlp = spacy.load(model)
    # Process the text through the loaded model
    doc = nlp(text_to_classify)

    # Check if "textcat" component is present in the pipeline
    if "textcat" not in nlp.pipe_names:
        raise ValueError("The 'textcat' component is not present in the pipeline.")

    textcat = doc.cats

    # Get the label with the highest score (highest confidence)
    sorted_label = sorted(textcat.items(), key=lambda x: x[1], reverse=True)


    return {'job title':text_to_classify,
            'best tab':sorted_label[0][0],
            'best confidence':sorted_label[0][1],
            'second best tab':sorted_label[1][0],
            'second best confidence':sorted_label[1][1]}
