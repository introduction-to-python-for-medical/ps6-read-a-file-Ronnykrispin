def create_codon_dict(file_path):
    codon_dict = {}  # מילון ריק לאחסון הקודונים
    with open(file_path, "r") as file:
        rows = file.readlines()  # קריאת כל השורות
    for row in rows:
        cells = row.strip().split("\t")  # הסרת תווים מיוחדים ופיצול לפי טאב (\t)
        if len(cells) >= 3:  # לוודא שיש מספיק נתונים בשורה
            codon = cells[0]  # הקודון נמצא בתא הראשון
            amino_acid = cells[2]  # קיצור חומצת האמינו בתא השלישי
            codon_dict[codon] = amino_acid  # עדכון המילון

    return codon_dict


# בדיקת הפונקציה
def test_create_codon_dict():
    result = create_codon_dict("data/codons.txt")  # מסלול לקובץ

    # בדיקת ערכים ספציפיים
    assert result['AAA'] == 'K', "Test Failed: 'AAA' should map to 'K'"
    assert result['AAC'] == 'N', "Test Failed: 'AAC' should map to 'N'"
    assert result['ACA'] == 'T', "Test Failed: 'ACA' should map to 'T'"
    assert result['ACC'] == 'T', "Test Failed: 'ACC' should map to 'T'"

    print("All tests passed successfully.")


# הרצת הבדיקה
test_create_codon_dict()
