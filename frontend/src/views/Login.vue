<template>
  <div class="login-container">
    <div class="login-box">
      <h1 style="font-size: 28px">实验室预约登录系统</h1>
      <div style="margin-top: 5px; margin-bottom: 20px">基于AI Agent智能预约系统</div>

      <el-form
        ref="formRef"
        :rules="rules"
        :model="form"
        label-width="auto"
        style="max-width: 600px"
      >
        <el-form-item prop="username">
          <el-input
            size="large"
            v-model="form.username"
            placeholder="请输入账号"
            :prefix-icon="User"
          />
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            size="large"
            v-model="form.password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            type="password"
            show-password
          />
        </el-form-item>
        <div>
          <el-button
            type="primary"
            size="large"
            style="width: 100%"
            @click="login"
            :loading="loadingValue"
            >登录</el-button
          >
          <div style="margin-top: 20px">
            <el-link href="/register" type="primary">没有账号？立即注册</el-link>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { User, Lock } from '@element-plus/icons-vue'
import { ElButton } from 'element-plus'
import { ElMessage } from 'element-plus'
import { loginApi } from '@/api/auth'
import { useUser } from '@/utils/user'

const { saveLoginData } = useUser()
const router = useRouter()
const formRef = ref()

const form = reactive({
  username: '',
  password: ''
})

const rules = {
  username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
}

const login = async () => {
  const valid = await formRef.value?.validate().catch(() => false)
  if (!valid) return

  loadingValue.value = true
  try {
    const res = await loginApi(form)

    if (res.code === 200) {
      saveLoginData(res.data)
      ElMessage.success('登录成功！')
      router.push('/home')
    }
  } catch {
    // The request interceptor displays the network or API error.
  } finally {
    loadingValue.value = false
  }
}

const loadingValue = ref(false)
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
  background-color: #fff;
}
</style>
