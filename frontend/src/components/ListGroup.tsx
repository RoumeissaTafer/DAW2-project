import { useForm } from "react-hook-form";
import { motion } from "framer-motion";

export default function ListGroup() {
  const { register, handleSubmit } = useForm();

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="p-6 max-w-md mx-auto bg-white rounded-xl shadow"
    >
      <form className="space-y-4">
        <div>
          <label className="block text-sm font-medium">Email</label>
          <input
            {...register("email")}
            type="email"
            className="w-full border p-2 rounded"
          />
        </div>

        <button className="w-full bg-blue-600 text-white p-2 rounded">
          Submit
        </button>
      </form>
    </motion.div>
  );
}
