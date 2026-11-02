<script setup>
import router from '@/router'
import { logout } from '@/utils/auth'
import {
  Menu as IconMenu,
  House,
  Setting,
  User,
  OfficeBuilding,
  Tickets,
  Document,
  ChatDotRound
} from '@element-plus/icons-vue'
import { useUser } from '@/utils/user'

const { userInfo } = useUser()

const handleCommand = (command) => {
  if (command === 'logout') {
    logout()
    router.push('/login')
  } else if (command === 'profile') {
    router.push('/profile')
  } else if (command === 'password') {
    router.push('/password')
  }
}
</script>

<template>
  <div>
    <el-container style="min-height: 100vh">
      <el-header
        style="
          display: flex;
          align-items: center;
          border-bottom: 1px solid #ddd;
          background-color: #fff;
        "
      >
        <div
          style="flex: 1; display: flex; align-items: center; font-size: 24px; font-weight: bold"
        >
          智能实验室预约系统
        </div>
        <div style="display: flex; align-items: center; cursor: pointer">
          <img :src="userInfo?.avatar" alt="" style="width: 30px; border-radius: 50%" />
          <el-dropdown @command="handleCommand">
            <div style="margin-left: 3px">{{ userInfo.name }}</div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="profile">个人信息</el-dropdown-item>
                <el-dropdown-item command="password">修改密码</el-dropdown-item>
                <el-dropdown-item divided command="logout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <el-menu
            router
            :default-active="router.currentRoute.value.path"
            style="height: 100%"
            default-active="home"
          >
            <el-menu-item index="home">
              <el-icon><icon-menu /></el-icon>
              系统首页
            </el-menu-item>
            <el-menu-item index="lablist" v-if="userInfo?.role === 'student'">
              <el-icon><OfficeBuilding /></el-icon>
              实验室列表
            </el-menu-item>
            <el-menu-item index="lab" v-if="userInfo?.role === 'admin'">
              <el-icon><House /></el-icon>
              实验室管理
            </el-menu-item>
            <el-menu-item index="equipment" v-if="userInfo?.role === 'admin'">
              <el-icon><Setting /></el-icon>
              设备列表管理
            </el-menu-item>
            <el-menu-item index="my-reservation" v-if="userInfo?.role === 'student'">
              <el-icon><Tickets /></el-icon>
              我的预约
            </el-menu-item>
            <el-menu-item index="audit-reservation" v-if="userInfo?.role === 'admin'">
              <el-icon><DocumentChecked /></el-icon>
              预约审核
            </el-menu-item>
            <el-menu-item index="user" v-if="userInfo?.role === 'admin'">
              <el-icon><User /></el-icon>
              用户管理
            </el-menu-item>
            <el-menu-item index="ai-chat">
              <el-icon><ChatDotRound /></el-icon>
              AI智能助手
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
