<script>
import axios from 'axios';

export default {
    data() {
        return {
            data: [],
            headers: [],
            file: null,
            loading: false
        };
    },
    methods: {
        handleFileUpload(event) {
            this.file = event.target.files[0];
        },
        uploadFile() {
            if (!this.file) {
                alert('Пожалуйста, выберите файл');
                return;
            }
            this.loading = true;
            const formData = new FormData();
            formData.append('file', this.file);
            axios.post('http://localhost:3000/api/upload', formData)
                .then(response => {
                    this.data = response.data;
                    if (this.data.length > 0) {
                        this.headers = Object.keys(this.data[0]);
                    }
                    this.loading = false;
                })
                .catch(error => {
                    console.error('Ошибка при загрузке файла:', error);
                    this.loading = false;
                });
        }
    }
};
</script>

<template>
    <div>
        <input type="file" accept=".xlsx" @change="handleFileUpload" />
        <button @click="uploadFile">Загрузить</button>
        <div v-if="loading">Загрузка...</div>
        <table class="table" v-if="data.length > 0">
            <thead>
                <tr>
                    <th v-for="(header, index) in headers" :key="index">{{ header }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, rowIndex) in data" :key="rowIndex">
                    <td v-for="(cell, cellIndex) in row" :key="cellIndex">{{ cell }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>