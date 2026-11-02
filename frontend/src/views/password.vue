<template>
  <div style="width: 50%">
    <el-card>
      <template #header>
        <div style="font-size: 16px; font-weight: bold">
          <span>修改密码</span>
        </div>
      </template>
      <el-form ref="formRef" :rules="rules" :model="form" label-width="100px" style="width: 100%">
        <el-form-item label="原密码" prop="oldPassword">
          <el-input
            type="password"
            show-password
            v-model="form.oldPassword"
            placeholder="请输入原密码"
          ></el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="newPassword">
          <el-input
            type="password"
            show-password
            v-model="form.newPassword"
            placeholder="请输入新密码"
          ></el-input>
        </el-form-item>
        <el-form ref="formRef" :rules="rules" :model="form" label-width="100px" style="width: 100%">
          <el-form-item label="确认新密码" prop="confirmPassword">
            <el-input
              type="password"
              show-password
              v-model="form.confirmPassword"
              placeholder="请确认新密码"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" :loading="submitting" @click="handleSubmit"
              >保存修改</el-button
            >
          </el-form-item>
        </el-form>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { updatePassword } from '@/api/user'
import { ref, reactive } from 'vue'
import { ElMessage } from 'element-plus'
import router from '@/router'
import { logout } from '@/utils/auth'

const formRef = ref(null)

const submitting = ref(false)

const form = reactive({
  oldPassword: '',
  newPassword: '',
  confirmPassword: ''
})

const validatePass = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请确认密码'))
  } else {
    if (value !== form.newPassword) {
      callback(new Error('两次密码输入不一致'))
    } else {
      callback()
    }
  }
}

const rules = {
  oldPassword: [{ required: true, message: '请输入原密码', trigger: 'blur' }],
  newPassword: [{ required: true, message: '请输入新密码', trigger: 'blur' }],
  confirmPassword: [{ validator: validatePass, message: '请确认新密码', trigger: 'blur' }]
}

const handleSubmit = async () => {
  const valid = await formRef.value?.validate().catch(() => false)
  if (!valid) return

  submitting.value = true
  try {
    const res = await updatePassword({
      old_password: form.oldPassword,
      new_password: form.newPassword
    })
    if (res.code === 200) {
      ElMessage.success('密码修改成功，请重新登录')
      logout()
      await router.push('/login')
    }
  } catch (error) {
    // API 错误提示由 request 拦截器统一显示。
    console.error('修改密码失败:', error)
  } finally {
    submitting.value = false
  }
}
</script>
