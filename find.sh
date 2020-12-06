echo "====== START >>>>>>> 3000s \n"
python test.py -s 3001 -e 4000
echo "====== START >>>>>>> 2000s \n"
python test.py -s 2001 -e 3000
echo "====== START >>>>>>> 1000s \n"
python test.py -s 1001 -e 2000
echo "====== START >>>>>>> 500s \n"
python test.py -s 501 -e 1000
echo "====== START >>>>>>> 100s \n"
python test.py -s 100 -e 500
echo "====== START >>>>>>> 1500-4500s \n"
python test.py -s 1500 -e 4500
echo "<<<<<<< FINISHED =======\n"