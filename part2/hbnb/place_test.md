# Place API – Test Cases
---

### 1. Create Place – Success
<img width="932" height="463" alt="image" src="https://github.com/user-attachments/assets/7a758251-c7c3-45e0-9ca1-2ea62f889b61" />


### 2. Create Place – Missing Required Field
missing title
<img width="930" height="364" alt="image" src="https://github.com/user-attachments/assets/e071a128-661c-48a2-bc92-a1c4a71c7921" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": title": "'title' is a required property
}
```

### 3. Create Place – Invalid Price (≤ 0)
<img width="932" height="407" alt="image" src="https://github.com/user-attachments/assets/e8d9a8c2-4b6f-41f1-9690-d0895eee8e6e" />

**Expected Result:**
- Status: `400 Bad Request`

```json
"errors": {
    "error": "Price must be a positive value"
  }
```
### 4. Create Place – Invalid Latitude
<img width="940" height="413" alt="image" src="https://github.com/user-attachments/assets/f3b73ee7-6047-4835-a66e-0c5a2183c394" />


**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "Latitude must be within -90.0 to 90.0"
}
```

### 5. Create Place – Invalid Longitude
<img width="918" height="401" alt="image" src="https://github.com/user-attachments/assets/8415e9fe-69d5-454c-8f3a-272e128d5145" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "Longitude must be within -180.0 to 180.0"
}
```

### 6. Create Place – Owner Does Not Exist
<img width="939" height="387" alt="image" src="https://github.com/user-attachments/assets/e25566d5-2674-4666-b06a-65c97e6c3dd3" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "Owner not found"
}
```
