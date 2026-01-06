"""Session Manager - 会话管理核心模块 [完整解决方案]"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


class SessionManager:
    """会话管理器 - 负责会话的创建、保存、加载和管理"""
    
    def __init__(self, storage_dir: str = "./data/sessions"):
        """
        初始化会话管理器
        
        Args:
            storage_dir: 会话数据存储目录
        """
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
    
    def create_session(self, user_id: str = "default") -> str:
        """
        创建新会话
        
        Args:
            user_id: 用户ID
            
        Returns:
            session_id: 新创建的会话ID
        """
        # 生成唯一的 session_id
        session_id = f"sess_{uuid.uuid4().hex[:8]}"
        
        # 创建会话数据结构
        session_data = {
            "session_id": session_id,
            "user_id": user_id,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "messages": []
        }
        
        # 保存到文件
        self._save_session(session_id, session_data)
        
        return session_id
    
    def add_message(self, session_id: str, role: str, content: str):
        """
        添加消息到会话
        
        Args:
            session_id: 会话ID
            role: 角色 ('user' 或 'assistant')
            content: 消息内容
        """
        # 加载会话
        session = self.load_session(session_id)
        
        # 添加新消息
        session["messages"].append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        
        # 更新时间
        session["updated_at"] = datetime.now().isoformat()
        
        # 保存
        self._save_session(session_id, session)
    
    def load_session(self, session_id: str) -> Dict:
        """
        加载会话数据
        
        Args:
            session_id: 会话ID
            
        Returns:
            session_data: 会话完整数据
            
        Raises:
            ValueError: 如果会话不存在
        """
        session_file = self.storage_dir / f"{session_id}.json"
        
        if not session_file.exists():
            raise ValueError(f"会话不存在: {session_id}")
        
        with open(session_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_messages(self, session_id: str) -> List[Dict]:
        """
        获取会话的所有消息
        
        Args:
            session_id: 会话ID
            
        Returns:
            messages: 消息列表
        """
        session = self.load_session(session_id)
        return session["messages"]
    
    def list_sessions(self) -> List[Dict]:
        """
        列出所有会话及其元数据
        
        Returns:
            sessions: 会话元数据列表（按创建时间倒序）
        """
        sessions = []
        
        # 遍历所有会话文件
        for session_file in self.storage_dir.glob("sess_*.json"):
            try:
                with open(session_file, 'r', encoding='utf-8') as f:
                    session_data = json.load(f)
                    
                # 提取元数据（不包含完整消息）
                sessions.append({
                    "session_id": session_data["session_id"],
                    "user_id": session_data.get("user_id", "unknown"),
                    "created_at": session_data["created_at"],
                    "updated_at": session_data["updated_at"],
                    "message_count": len(session_data["messages"])
                })
            except Exception as e:
                print(f"⚠️  加载会话失败 {session_file.name}: {e}")
        
        # 按创建时间倒序排序（最新的在前）
        sessions.sort(key=lambda x: x["created_at"], reverse=True)
        
        return sessions
    
    def _save_session(self, session_id: str, data: Dict):
        """
        内部方法：保存会话数据到文件
        
        Args:
            session_id: 会话ID
            data: 会话数据
        """
        session_file = self.storage_dir / f"{session_id}.json"
        
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
