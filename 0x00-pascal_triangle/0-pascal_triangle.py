#!/usr/bin/python3
def pascal_triangle(n):
    # إذا كانت قيمة n <= 0، ارجع قائمة فارغة
    if n <= 0:
        return []
    
    # إنشاء قائمة لتخزين الصفوف
    triangle = []

    # بناء مثلث باسكال
    for i in range(n):
        # إنشاء الصف الحالي
        row = [1] * (i + 1)  # ملء الصف بالأعداد 1

        # حساب عناصر الصف باستخدام العناصر من الصف السابق
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # إضافة الصف إلى مثلث باسكال
        triangle.append(row)

    # إرجاع مثلث باسكال
    return triangle
