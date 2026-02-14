# Reference Index (Current Project)

## 命名规范

- 文件命名：`场景_语言_架构.md`
- 例如：`backend_python_flask-microservice.md`

## 当前项目枚举

1. `frontend_typescript_nextjs-app-router.md`
2. `backend_typescript_nextjs-route-handlers.md`
3. `backend_python_flask-microservice.md`
4. `backend_typescript_json-file-storage.md`
5. `platform_typescript-python_docker-single-container.md`
6. `fullstack_typescript-python_modular-monolith-plus-sidecar.md`
7. `other_typescript_jest-testing.md`

## 分步加载规则

1. 先读取本文件，识别候选参考文件。
2. 按用户范围加载：
   - `frontend`：加载 `frontend_typescript_nextjs-app-router.md`
   - `backend`：加载 `backend_typescript_nextjs-route-handlers.md`、`backend_python_flask-microservice.md`、`backend_typescript_json-file-storage.md`、`platform_typescript-python_docker-single-container.md`
   - `other`：加载 `other_typescript_jest-testing.md`
   - `all`：加载全部文件
3. 每个已加载文件必须提取并落地三类内容：
   - 重构思路
   - 合规思路
   - 最佳实践
