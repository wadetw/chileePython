# 俄羅斯方塊專案

本檔案記錄了此專案在 Gemini CLI 環境中的相關設定。

## GEMINI CLI 的 System 和 User Prompt 設定

- **System Prompt**: 這是指導 AI 模型行為的核心指令，通常由 Gemini CLI 工具本身預設，定義了 AI 的角色、能力、限制與互動風格 (例如，"你是一位專業的軟體工程師...")。使用者通常無法直接修改此設定。
- **User Prompt**: 這就是您在對話中輸入的指令或問題，例如 `請幫我建立一個檔案`。

這兩者是 Gemini CLI 運作的基礎，而非專案內的特定設定檔案。

## GEMINI CLI 的 Project Prompt 設定

Project Prompt（專案提示）是透過在專案根目錄或子目錄中放置 `GEMINI.md` 檔案來實現的。這個檔案會提供關於目前專案的特定背景資訊給 AI，讓它能更精準地理解您的需求。

以下是從您專案根目錄 `GEMINI.md` 讀取到的內容：

```markdown
## 專案的設定
- 這是一個python flask的專案

## 虛擬環境
- 使用uv建立的虛擬環境
- 所有python套件安裝請使用`uv add 套件名稱`

## 工作目錄描述
- chileePython是上課用的主目錄

## 目前次專案的工作目錄
- chileePython/貪食蛇1
```

## AI遵守行為
- 所有回覆請使用繁體中文版
- 你是一個有耐心的python老師
