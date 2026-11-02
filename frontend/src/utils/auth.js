//存储token，存储用户信息，获取token，用户信息，删除token

const TOKEN_KEY = 'token'
const USER_KEY = 'userIndo'

export function getToken() {
  return localStorage.getItem(TOKEN_KEY)
}

export function setToken(token) {
  localStorage.setItem(TOKEN_KEY, token)
}

export function removeToken() {
  localStorage.removeItem(TOKEN_KEY)
}

export function getUserInfo() {
  const str = localStorage.getItem(USER_KEY)
  return str ? JSON.parse(str) : null
}

export function setUserInfo(userinfo) {
  localStorage.setItem(USER_KEY, JSON.stringify(userinfo))
}

export function removeUserInfo() {
  localStorage.removeItem(USER_KEY)
}

//登出
export function logout() {
  removeToken()
  removeUserInfo()
}
