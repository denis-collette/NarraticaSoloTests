'use client'

import React, { useState } from 'react'

export default function RegisterPage() {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        password2: '',
    })

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
            const response = await fetch('http://localhost:8000/api/auth/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: formData.username,
                    email: formData.email,
                    password: formData.password,
                    password2: formData.password2,
                }),
            })

        const data = await response.json()
        console.log('Response:', data)
        if (response.ok) {
            alert('Registration successful!')
        } else {
            alert(`Error: ${JSON.stringify(data)}`)
        }
        } catch (error) {
        console.error('Registration failed:', error)
        }
    }

    return (
        <div className="p-6 max-w-md mx-auto">
            <h1 className="text-2xl font-bold mb-4">Register</h1>
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
                <input
                name="username"
                type="text"
                placeholder="Username"
                value={formData.username}
                onChange={handleChange}
                className="border p-2"
                required
                />
                <input
                name="email"
                type="email"
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
                <input
                name="password2"
                type="password"
                placeholder="Confirm Password"
                value={formData.password2}
                onChange={handleChange}
                className="border p-2"
                required
                />
                <button type="submit" className="bg-black text-white p-2 rounded">
                Register
                </button>
            </form>
        </div>
    )
}
