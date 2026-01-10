# User API – Test Cases
---

### 1. Create User – Success Case
<img width="929" height="418" alt="لقطة شاشة 2026-01-10 114331" src="https://github.com/user-attachments/assets/6ae965a1-e750-4d65-9d96-89c3d6c39803" />

### 2. Create User – Duplicate Email
<img width="936" height="344" alt="لقطة شاشة 2026-01-10 114703" src="https://github.com/user-attachments/assets/15f17d8a-228c-4c2e-925c-354005a3e424" />


**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "Email already registered"
}
```

### 3. Create User – Missing Required Field
Missing email
<img width="915" height="405" alt="لقطة شاشة 2026-01-10 114800" src="https://github.com/user-attachments/assets/7a9ee3a3-b2ec-4290-81a6-5670ee4b2339" />

**Expected Result:**
- Status: `400 Bad Request`

```json
"errors": {
    "email": "'email' is a required property"
  }
```
### 4. Create User – Invalid Email Format
<img width="922" height="339" alt="لقطة شاشة 2026-01-10 114923" src="https://github.com/user-attachments/assets/d64ea18f-2afd-4a32-a3b9-8fa885b9e2b1" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "Invalid email format"
}
```

### 5. Create User – Name Too Long (>50 chars)
<img width="928" height="400" alt="لقطة شاشة 2026-01-10 115012" src="https://github.com/user-attachments/assets/e76466c3-89de-43af-bef2-074654849275" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "First name is required and must be under 50 characters"
}
```

## Get Users

### 6. Get All Users – Success
<img width="923" height="338" alt="لقطة شاشة 2026-01-10 115127" src="https://github.com/user-attachments/assets/36b899aa-3f2c-4849-a004-b61749145b94" />

### 7. Get User by ID – Success
<img width="940" height="290" alt="لقطة شاشة 2026-01-10 115205" src="https://github.com/user-attachments/assets/cc36d150-0b4e-4b23-90e8-12fe55ff10b8" />

### 8. Get User by ID – Not Found
<img width="942" height="823" alt="لقطة شاشة 2026-01-10 115326" src="https://github.com/user-attachments/assets/37eadb16-fb63-4628-9a7b-213dbfd2c26f" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "User not found"
}
```
