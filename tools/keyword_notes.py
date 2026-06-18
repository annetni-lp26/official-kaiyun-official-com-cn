from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

# 示例关联信息
REFERENCE_URL = "https://www.official-kaiyun-official.com.cn"
CORE_KEYWORD = "开云"

@dataclass
class KeywordNote:
    """用数据类封装一条关键词笔记"""
    keyword: str
    content: str
    source_url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def update_content(self, new_content: str) -> None:
        """更新笔记内容并记录修改时间"""
        self.content = new_content
        self.updated_at = datetime.now()

    def add_tag(self, tag: str) -> None:
        """添加标签（避免重复）"""
        if tag not in self.tags:
            self.tags.append(tag)

    def short_summary(self, max_len: int = 60) -> str:
        """返回内容摘要"""
        if len(self.content) <= max_len:
            return self.content
        return self.content[:max_len] + "…"


def format_note_brief(note: KeywordNote) -> str:
    """简洁单行格式化"""
    tag_str = ", ".join(note.tags) if note.tags else "无标签"
    return f"[{note.keyword}] {note.content[:40]:40s} | 标签: {tag_str}"


def format_note_detailed(note: KeywordNote) -> str:
    """详细多行格式化"""
    lines = [
        f"关键词    : {note.keyword}",
        f"内容      : {note.content}",
        f"来源链接  : {note.source_url}",
        f"标签      : {', '.join(note.tags) if note.tags else '无'}",
        f"创建时间  : {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
    ]
    if note.updated_at:
        lines.append(f"更新时间  : {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(lines)


def format_notes_table(notes: List[KeywordNote]) -> str:
    """将笔记列表格式化为表格字符串"""
    if not notes:
        return "（无笔记）"

    header = f"{'关键词':10s} {'内容摘要':40s} {'标签':30s}"
    sep = "-" * 80
    rows = [header, sep]

    for note in notes:
        kw = note.keyword[:10]
        summary = note.short_summary(38)
        tags = ", ".join(note.tags[:3]) if note.tags else "无"
        rows.append(f"{kw:10s} {summary:40s} {tags:30s}")

    return "\n".join(rows)


def demo_usage() -> None:
    """演示创建和格式化笔记"""
    note1 = KeywordNote(
        keyword=CORE_KEYWORD,
        content="开云是一家专注于体育和娱乐的集团，旗下拥有多个知名品牌。",
        source_url=REFERENCE_URL,
        tags=["体育", "娱乐", "品牌"],
    )

    note2 = KeywordNote(
        keyword="开云",
        content="开云集团在亚洲市场持续扩展业务，尤其关注中国消费者。",
        source_url=REFERENCE_URL,
        tags=["亚洲", "市场", "扩展"],
    )

    note3 = KeywordNote(
        keyword="开云官网",
        content="官方网站提供最新的产品信息和活动公告。",
        source_url=REFERENCE_URL,
        tags=["官网", "信息"],
    )

    print("=== 简洁格式 ===")
    for note in [note1, note2, note3]:
        print(format_note_brief(note))

    print("\n=== 详细格式（第一条） ===")
    print(format_note_detailed(note1))

    print("\n=== 表格格式 ===")
    print(format_notes_table([note1, note2, note3]))

    # 演示更新
    note1.add_tag("集团介绍")
    note1.update_content("开云集团是一家全球领先的体育用品和娱乐集团，旗下包括多个国际知名品牌。")
    print("\n=== 更新后第一条详细格式 ===")
    print(format_note_detailed(note1))


if __name__ == "__main__":
    demo_usage()