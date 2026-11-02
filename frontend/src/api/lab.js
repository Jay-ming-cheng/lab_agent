import request from '@/utils/request'

//分页获取列表
export function getLabPageList(params) {
  return request({
    url: `/api/lab/list`,
    method: `get`,
    params
  })
}

//新建
export function createLabApi(data) {
  return request({
    url: `/api/lab`,
    method: `post`,
    data
  })
}

//更新
export function updateLabApi(labId, data) {
  return request({
    url: `/api/lab/${labId}`,
    method: `put`,
    data
  })
}

//删除
export function deleteLabApi(labId) {
  return request({
    url: `/api/lab/${labId}`,
    method: `delete`
  })
}

/**
 * 根据ID查询实验室详情
 * @param {Number} lab_id
 * @returns
 */
export function getLab(lab_id) {
  return request({
    url: `/api/lab/${lab_id}`,
    method: 'get'
  })
}
