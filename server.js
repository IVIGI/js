const express = require('express');
const cors = require('cors');
const XLSX = require('xlsx');
const multer = require('multer');
const fs = require('fs');
const app = express();
const port = 3000;

// Создаем папку uploads, если ее нет
const uploadDir = 'uploads/';
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir);
}

// Настраиваем multer для загрузки файлов
const upload = multer({ dest: uploadDir, limits: { fileSize: 10 * 1024 * 1024 } }); // Лимит 10 МБ

app.use(cors());

// Эндпоинт для загрузки файла
app.post('/api/upload', upload.single('file'), (req, res) => {
    try {
        if (!req.file) {
            return res.status(400).send('Файл не загружен');
        }
        if (!req.file.originalname.endsWith('.xlsx')) {
            fs.unlinkSync(req.file.path); // Удаляем неподходящий файл
            return res.status(400).send('Разрешены только файлы .xlsx');
        }
        const filePath = req.file.path;
        const workbook = XLSX.readFile(filePath);
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const jsonData = XLSX.utils.sheet_to_json(worksheet);
        res.json(jsonData);
        fs.unlinkSync(filePath); // Удаляем файл после обработки
    } catch (error) {
        res.status(500).send('Ошибка при обработке файла');
    }
});

app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});