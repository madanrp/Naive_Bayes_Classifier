#Solutions to part III

1. Precision and recall for Part I
----------------------------------
    a. Sentiment Data
    -----------------
        class NEG
        --------- 
        Precision = 0.8298507462686567
        Recall = 0.8735271013354281
        F-score = 0.8511289705319556

        class POS
        ---------
        Precision = 0.8634435962680237
        Recall = 0.8170144462279294
        F-score = 0.8395876288659793

    b. Spam Data
    ------------
        class HAM
        ---------
        Precision = 0.9869346733668342
        Recall = 0.982
        F-score = 0.9844611528822055

        class SPAM
        ----------
        Precision = 0.9510869565217391
        Recall = 0.9641873278236914
        F-score = 0.957592339261286
    

2. Precision and Recall for Part II
-----------------------------------
    SVM
    ---
        a. Sentiment Data
        -----------------
            class POS
            ---------
            Precision = 0.8351063829787234
            Recall = 0.8820224719101124
            F-score = 0.8579234972677595
            class NEG
            ---------
            Precision = 0.8778054862842892
            Recall = 0.8295365278868814
            F-score = 0.8529886914378029

       b. Spam Data
       ------------
            class SPAM
            ----------
            Precision = 0.9568106312292359
            Recall = 0.7933884297520661
            F-score = 0.8674698795180723

            class HAM
            ---------
            Precision = 0.9293785310734464
            Recall = 0.987
            F-score = 0.9573229873908826

 
    MEGAM
    -----
        a. Sentiment Data
        -----------------
            class NEG
            ---------
            Precision = 0.8505311077389985
            Recall = 0.8805970149253731
            F-score = 0.86530297182555

            class POS
            ---------
            Precision = 0.8734388009991674
            Recall = 0.8418940609951846
            F-score = 0.8573763792398855

        b. Spam Data
        ------------
            class SPAM
            ----------
            Precision = 0.9237057220708447
            Recall = 0.9338842975206612
            F-score = 0.9287671232876713

            class HAM
            ---------
            Precision = 0.9759036144578314
            Recall = 0.972
            F-score = 0.973947895791583


3) When 10% of input data is used
---------------------------------
    When only 10% of input data is used, precision of POS/HAM class descreases and recall increases. F1-score decreases too.
    Whereas for NEG/SPAM, precision increases and recall decreases. F1-score increases proportionately.
    This happens because
        - overfitting and hence does not generalize
        - Now more documents are going to NEG/SPAM bin and hence precision of these classes increase
        - However recall decreases because most of them are classified wrong 
