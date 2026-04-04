# 🤝 Contributing Guidelines

> ขอบคุณที่สนใจร่วมพัฒนา BDL Apex Prime! คู่มือนี้จะช่วยให้คุณมีส่วนร่วมอย่างมีประสิทธิภาพ

---

## 📋 ขั้นตอนการมีส่วนร่วม

### 1. Fork Repository
```bash
fork BDL-Apex/God-Tier-System-Instructions
```

### 2. Clone Forked Repository
```bash
git clone https://github.com/YOUR-USERNAME/God-Tier-System-Instructions.git
cd God-Tier-System-Instructions
```

### 3. สร้าง Branch ใหม่
```bash
git checkout -b feature/your-feature-name
```

### 4. ทำการแก้ไขหรือเพิ่มไฟล์

---

## 🛠️ Requirements สำหรับ Prompt ใหม่

### ✅ Must Have:

#### 1. XML Tags
ทุก Prompt ต้องมี XML Metadata:
```xml
<prompt>
  <name>Prompt Name</name>
  <version>1.0</version>
  <author>Your Name</author>
  <framework>CO-STAR</framework>
</prompt>
```

#### 2. CO-STAR Framework Elements
ต้องมี 6 องค์ประกอบนี้:
- **C (Context):** บริบทแวดล้อม/สถานการณ์
- **O (Objective):** เป้าหมายที่ชัดเจน
- **S (Style):** สไตล์การเขียน (Technical, Narrative, Academic, etc.)
- **T (Tone):** น้ำเสียง (Professional, Casual, Hyper-intelligent, etc.)
- **A (Audience):** กลุ่มเป้าหมาย (Developer, Manager, Student, etc.)
- **R (Response):** รูปแบบผลลัพธ์ (Markdown, JSON, Code, Essay, etc.)

#### 3. Confidence Score
ประเมินความเชื่อมั่นของ Prompt (0.0 - 1.0):
```
✅ >= 0.85: Ready for production
⚠️  0.75-0.84: Good, minor improvements needed
🔴 < 0.75: Needs rework
```

#### 4. Real Examples
ต้องรวมตัวอย่างการใช้งานจริง:
- **Before:** ตัวอย่างคำถาม/Input
- **After:** ผลลัพธ์ที่คาดหวัง (Expected Output)
- ✅ มี 2+ ตัวอย่างต่อ Prompt

#### 5. Hallucination Control Protocol
ต้องระบุวิธีการควบคุมการสร้างข้อมูลที่ไม่จริง:
- ตรวจสอบ Fact?
- ใช้ "Insufficient Data" rule?
- Reference ที่ชัดเจน?

---

## 📝 Template: Prompt Submission

```markdown
# [Prompt Name]

## 📊 Metadata
- **Version:** 1.0
- **Author:** [Your Name]
- **Framework:** CO-STAR
- **Confidence Score:** 0.XX
- **Date Created:** YYYY-MM-DD

## 🧠 Content

### Context (C)
[ระบุบริบท]

### Objective (O)
[ระบุเป้าหมาย]

### Style (S)
[ระบุสไตล์]

### Tone (T)
[ระบุน้ำเสียง]

### Audience (A)
[ระบุกลุ่มเป้าหมาย]

### Response (R)
[ระบุรูปแบบผลลัพธ์]

## 🔍 Quality Checks

### Hallucination Control
- [ ] มีกลไกตรวจสอบข้อเท็จจริง
- [ ] ชัดเจนว่าเมื่อไหร่ใช้ "Insufficient Data"
- [ ] Reference มีความชัดเจน

### Examples

#### Example 1:
**Input:** [ตัวอย่างคำถาม]
**Expected Output:** [ผลลัพธ์ที่คาดหวัง]

#### Example 2:
**Input:** [ตัวอย่างคำถาม]
**Expected Output:** [ผลลัพธ์ที่คาดหวัง]

## 📋 Checklist
- [ ] XML Structure ถูกต้อง
- [ ] มี CO-STAR Elements ครบถ้วน
- [ ] Confidence Score ระบุแล้ว
- [ ] มีตัวอย่าง 2+ ตัวอย่าง
- [ ] Hallucination Control Protocol ชัดเจน
- [ ] ไฟล์อยู่ในโฟลเดอร์ที่ถูกต้อง

---

## 📂 Directory Guidelines

### Prompt Storage:
- **role-based-prompts/**: Prompt สำหรับบทบาทเฉพาะ
- **core-frameworks/**: Framework หลัก
- **xml-templates/**: Template XML ว่าง

### Naming Convention:
```
[PURPOSE]_[ROLE]_[VERSION].md

ตัวอย่าง:
- system-instruction_developer_v1.md
- prompt_strategist_v2.md
```

---

## 🚀 Pull Request Process

### ก่อนส่ง PR:
1. Commit changes:
   ```bash
   git add .
   git commit -m "[ADD/UPDATE] Describe your changes"
   ```

2. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. เปิด Pull Request บน GitHub

### PR Template:
```markdown
## 📝 Description
[อธิบายการเปลี่ยนแปลงของคุณ]

## 🎯 Type of Change
- [ ] New Prompt
- [ ] Update Existing Prompt
- [ ] Fix/Bug
- [ ] Documentation

## ✅ Checklist
- [ ] XML Structure ตรวจสอบแล้ว
- [ ] CO-STAR Elements ครบถ้วน
- [ ] Confidence Score >= 0.75
- [ ] Examples รวมแล้ว (2+)
- [ ] Hallucination Control ชัดเจน
- [ ] README อัพเดทแล้ว (ถ้าเกี่ยวข้อง)

## 📚 Related Issues
Closes #(issue number)
```

---

## ⚖️ Code of Conduct

- ✅ เคารพความคิดเห็นของผู้อื่น
- ✅ ให้ Feedback อย่างสร้างสรรค์
- ✅ ตรวจสอบแฟกต์ก่อนส่ง
- ❌ ห้ามคำด่า หรือพฤติกรรมไม่สุภาพ

---

## 💡 Questions?

หากมีคำถาม โปรดเปิด GitHub Issue หรือติดต่อ maintainers

---

**ขอบคุณที่มีส่วนร่วม! 🎉**

_Last Updated: 2026-04-04_