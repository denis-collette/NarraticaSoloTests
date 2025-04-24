import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/", // Ensure this matches your backend URL
    timeout: 5000,
});

export default api;
