def create_codon_dict(file_path):
    d = {}
    try:
        with open(file_path, 'r') as file:  # פתיחת הקובץ בצורה בטוחה
            for row in file:  # מעבר שורה-שורה
                cells = row.strip().split('\t')  # חלוקה לפי טאב (או רווחים לפי הצורך)
                if len(cells) >= 2:  # בדיקה אם יש מספיק שדות בשורה
                    codon = cells[0]
                    amino_acid = cells[1]
                    d[codon] = amino_acid
    except FileNotFoundError:
        print(f"שגיאה: הקובץ {file_path} לא נמצא.")
    except Exception as e:
        print(f"קרתה שגיאה: {e}")
    return d

