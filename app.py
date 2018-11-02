from flask import Flask, render_template, request
import os
os.environ["KERAS_BACKEND"] = "theano"
import train_model_for_operation_prediction
import predict_operation_and_operands_to_find_answer




app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def word_problem_solver():
    errors = []
    results = {}
    if request.method == "POST":
        try:
            questionText = request.form['question']
            #call model

            train ="train.txt"
            testfile ="test.txt"
            para ="parameters_GRU_21112017_tensorflow_pre_padding_0.5dropout"
            model ="model_json_GRU_21112017_tensorflow_pre_padding_0.5dropout.json"
            weights = "weights_GRU_21112017_tensorflow_pre_padding_0.5dropout"
            #question = "question_to_answer.txt"
            question = questionText

            print (question)
#train_model_for_operation_prediction.main(train,testfile,model,weights)
            equation, answer = predict_operation_and_operands_to_find_answer.main(model,weights,para,question)

            print (equation)

            print (answer)

            print(questionText)
            results['question'] = questionText
            results['answers'] = [equation, answer]
        except Exception as e:
            print (e)
            errors.append(
                "Error occurred while processing your request....Please try again.."
            )
    return render_template('homepage.html', title="Welcome to Word Problem Solver", errors=errors, results=results)


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))	
    app.run(port=port)
