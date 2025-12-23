
import { useForm } from "react-hook-form";
import { useState } from "react";
import { Eye, EyeOff } from "lucide-react";
import { motion } from "framer-motion";
import logo from "../assets/logo.jpg";
import {FaFileAlt,FaFileImage} from 'react-icons/fa';

type FormData = {
  email: string;
  password: string;
  confirmPassword?: string; 
  username:string;
};

export default function MedicalAuth() {
  //const [username, setUsername] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [isLogin, setIsLogin] = useState(true); 
  const [role, setRole] = useState("");
  const [photo, setPhoto] = useState<File | null>(null);
  const [bio, setBio] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    watch,
  } = useForm<FormData>();

  const onSubmit = async (data: FormData) => { await new Promise((r) => setTimeout(r, 1200));} 


  const password = watch("password", "");

  return (
    <div className=" min-h-screen flex items-center justify-center bg-gradient-to-t from-white to-[#7BBDE8] px-4">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        className="m-4 w-full max-w-md bg-white rounded-3xl shadow-xl p-8"
      >
      
        <div className="flex flex-col items-center mb-6">
          <div className="rounded-full mb-3  shadow-sm ">
            <img
              src={logo}
              alt="Logo"
              className="w-20 h-20 rounded-full" 
            />
          </div>

          <h1 className="text-2xl font-bold text-gray-800 font-mono">
            {isLogin ? "MedSymposium Login" : "MedSymposium Sign Up"}
          </h1>
          <p className="text-sm text-gray-500 mt-1 text-center">
            {isLogin
              ? "Secure access for healthcare staff"
              : "Create a new account to access the portal"}
          </p>
        </div>

       
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
         {!isLogin && (
          <div>
              <label className="label">Username</label>
              <input
                type="text"
                placeholder="Enter your username"
                className={`input ${errors.username ? "input-error" : ""}`}
                required
                {...register("username", {
                required: "username is required",
                pattern: {
                  value: /^\S+@\S+$/,
                  message: "Invalid username format",
                },
                })}
              />
              {errors.username && <p className="error">{errors.username.message}</p>}
            </div>
         )}
          <div>
            <label className="label">Email Address</label>
            <input
              type="email"
              className={`input ${errors.email ? "input-error" : ""}`}
              placeholder="doctor@hospital.com"
              required
              {...register("email", {
                required: "Email is required",
                pattern: {
                  value: /^\S+@\S+$/,
                  message: "Invalid email format",
                },
              })}
            />
            {errors.email && <p className="error">{errors.email.message}</p>}
          </div>

         
          <div>
            <label className="label">Password</label>
            <div className="relative">
              <input
                type={showPassword ? "text" : "password"}
                className={`input pr-10 ${errors.password ? "input-error" : ""}`}
                placeholder="••••••••"
                required
                {...register("password", {
                  required: "Password is required",
                  minLength: {
                    value: 6,
                    message: "Minimum 6 characters",
                  },
                })}
                
              />
              
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-3 text-gray-400 hover:text-sky-600"
              >
                {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
              </button>
              
            </div>
            {errors.password && <p className="error">{errors.password.message}</p>}
          </div>
         
      

          
          {!isLogin && (
            <>
            <div>
              <label className="label">Confirm Password</label>
              <input
                type={showPassword ? "text" : "password"}
                className={`input pr-10 ${errors.confirmPassword ? "input-error" : ""}`}
                placeholder="••••••••"
                {...register("confirmPassword", {
                  required: "Confirm password is required",
                  validate: (value) =>
                    value === password || "Passwords do not match",
                })}
              />
            
              {errors.confirmPassword && (
                <p className="error">{errors.confirmPassword.message}</p>
              )}
            </div>
             <div>
        <label className="block text-sm font-medium text-slate-700 mb-1">
          Role
        </label>
        <select
        required
          value={role}
          onChange={(e) => setRole(e.target.value)}
          className=" w-full rounded-3 border border-slate-200 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-sky-400  "
        >
          <option value="" >Select a role</option>
          <option value="organizer">Organizer</option>
          <option value="author">Author</option>
          <option value="participant">Participant</option>
          <option value="Workshop animator">Workshop Animator</option>
        </select>
      </div>
      <div >
        <label className="block text-sm font-medium text-slate-700 mb-1">
          Profile photo
        </label>
        <div className="flex">
          <FaFileImage className="text-sky-600 mt-2 mr-2"/>
          <input
          type="file"
          accept="image/*"
          required
          onChange={(e) => setPhoto(e.target.files?.[0] || null)}
          className="w-full text-sm text-slate-600
                     file:mr-4 file:py-2 
                     file:rounded file:border-0
                     file:bg-sky-50 file:text-sky-600
                      hover:file:bg-sky-100" 
        />
        </div>
        
      </div>
      <div>
        <label className="block text-sm font-medium text-slate-700 mb-1">
          Biography
        </label>
        <textarea
          required
          value={bio}
          onChange={(e) => setBio(e.target.value)}
          rows={3}
          placeholder="Tell us about yourself..."
          className="w-full rounded-2xl border border-slate-200 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-sky-400"
        />
      </div>
            
          </>
          )}

         
          <button className="btn bg-[#0A4174] hover:!bg-[#7BBDE8] " disabled={isSubmitting}>
            {isSubmitting ? (isLogin ? "Logging in..." : "Signing up...") : isLogin ? "Sign In" : "Sign Up"}
          </button>
        </form>

       
        <p className="text-xs text-center text-gray-400 mt-4">
          {isLogin ? "Don't have an account?" : "Already have an account?"}{" "}
          <button
            className="text-sky-600 font-medium hover:underline"
            onClick={() => setIsLogin(!isLogin)}
          >
            {isLogin ? "Sign Up" : "Login"}
          </button>
        </p>

        
        <p className="text-xs text-center text-gray-400 mt-6">
          © 2026 MedSymposium System — Secure & Confidential
        </p>
      </motion.div>
    </div>
  );
}

