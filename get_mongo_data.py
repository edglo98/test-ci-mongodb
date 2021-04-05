import os
os.system('mongoexport --uri mongodb+srv://edglo:HolaMongo1@cluster0.suzwc.mongodb.net/UTM-Perfile --collection categories --type csv --fields name,color --out ./extmongo.csv')