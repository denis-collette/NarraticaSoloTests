'use client'

import React, { useState } from 'react'

export default function LoginPage() {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    })

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
            const response = await fetch('http://localhost:8000/api/auth/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email: formData.email,
                    password: formData.password,
                }),
            })

            const data = await response.json()
            console.log('Response:', data)

            if (response.ok) {
                alert('Login successful!')
                // Save the ******* token dumbass! With localStorage or a context for authentication said this GPT guy...
                localStorage.setItem('authToken', data.token)
            } else {
                alert(`Error: ${JSON.stringify(data)}`)
            }
        } catch (error) {
            console.error('Login failed:', error)
        }
    }

    return (
        <div className="p-6 max-w-md mx-auto">
            <h1 className="text-2xl font-bold mb-4">Login</h1>
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
                <input
                    name="email"
                    type="text"
                    placeholder="Email"
                    value={formData.email}
                    onChange={handleChange}
                    className="border p-2"
                    required
                />
                <input
                    name="password"
                    type="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                    className="border p-2"
                    required
                />
                <button type="submit" className="bg-black text-white p-2 rounded">
                    Login
                </button>
            </form>
        </div>
    )
}
