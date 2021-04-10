arch -x86_64 python3 Optimizer_mac_hash.py $1
status=$?
if [ $status = 1 ]; then
    echo "Optimizer failed while hashing the circuit"
fi

rm "temp_eval.csv"

python3 Optimizer_mac_ml.py
status=$?
if [ $status = 1 ]; then
    echo "Optimizer failed while running machine learning analysis"
fi

arch -x86_64 python3 Optimizer_mac_final.py $1 temp_pred.csv
status=$?
if [ $status = 1 ]; then
    echo "Optimizer failed while running final optimization steps"
fi

rm "temp_eval_hashed.csv"
rm "temp_pred.csv"