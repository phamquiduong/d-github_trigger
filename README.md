# GITHUB TRIGGER
- Dự án thông báo đến các kênh chat khi thực hiện thao tác với Github

<br>

### Các Github trigger đang hỗ trợ
- Pull requests
- Pull request review comments
- Pull request reviews
- Workflow runs

<br>

### Các kênh thông báo đang hỗ trợ
- Telegram

<br>

### Deploy
- Hiện tại project đang được deploy bằng Vercel serverless
- Setup các biến môi trường
    - `[Tên dự án]_TELEGRAM_CHAT_ID`
    - `[Tên dự án]_TELEGRAM_BOT_TOKEN`

    - **Lưu ý**: Tên dự án phải đúng theo quy tắc của Vercel. Chỉ sử dụng chữ, số và dấu gạch dưới `_`


<br>

### Cài đặt dự án với Github webhook
- Đường dẫn: `http://[Server host]/[Tên dự án]`
- Bật các trigger mà dự án hỗ trợ

<br>

---

<p align="right">
    <sup>
        © Phạm Quí Dương • Cập nhật lần cuối: 28/09/2025
    </sup>
</p>
