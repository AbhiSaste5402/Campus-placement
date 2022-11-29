from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__, template_folder='template')
svm_model=pickle.load(open('Placementinternship.pickle', 'rb'))



@app.route('/')
def home():
    return render_template("home.html")



@app.route('/send', methods=['GET','POST'])
def predict():
    if request.method == "POST" :
        ssc_p = request.form['ssc_p']
        hsc_p = request.form['hsc_p']


        hsc_s = request.form['hsc_s1']
        degree_p = request.form['degree_p']
        degree_t = request.form['degree_t1']
        workex = request.form['workex1']
        etest_p = request.form['etest_p']
        specialisation = request.form['specialisation1']
        mba_p = request.form['mba_p']
       

        
        if degree_t == 'Sci&Tech':
            degree_t1 = 2
        elif degree_t == 'Comm&Mgmt':
            degree_t1 = 0
        else:
            degree_t1 = 1 
    
        if workex == 'Yes':
            workex1 = 1
        else:
            workex1 = 0
        
        if hsc_s == 'Commerce':
            hsc_s1 = 1
        elif hsc_s == 'Science':
            hsc_s1 = 2
        else:
            hsc_s1 = 0
        
        if specialisation == 'Mkt&HR':
            specialisation1 = 1
        else:
            specialisation1 = 0
    
        Pred_args=[ssc_p,hsc_p,hsc_s1,degree_p,degree_t1,workex1,etest_p,specialisation1,mba_p]
        pred_args=np.array(Pred_args)
        pred_args=pred_args.reshape(1,-1)
        
        y_pred=svm_model.predict(pred_args)
        y_pred=y_pred[0]
        if y_pred == 0:
            return render_template('show.html',res="Your Chances are less, you should work hard") 
        else:
            return render_template('show.html',res="By evaluating your scores and past experience, you have good chances of getting placements")
    
    
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)