# Algorithm Study

알고리즘 및 코딩테스트 문제 풀이를 기록하고 관리하는 공동 저장소입니다.

백준, 프로그래머스, SWEA, LeetCode의 풀이를 **GitHub 계정별로 분리하여 관리**하며, 브라우저 확장 프로그램을 통해 정답 코드를 자동으로 업로드합니다.

## Members

| 이름 | GitHub | Language |
| --- | --- | --- |
| 예슬 | [@sonyeseul63](https://github.com/sonyeseul63) | Java, Python |
| 민주 | [@Hanminjoo72](https://github.com/Hanminjoo72) | Python |

## Repository Structure

```text
ALGO_STUDY/
├── sonyeseul63/
│   ├── BOJ/
│   ├── PROG/
│   ├── SWEA/
│   └── LeetCode/
│
├── Hanminjoo72/
│
└── README.md
```

- 최상위 디렉터리는 각 팀원의 **GitHub 사용자명**을 사용합니다.
- 플랫폼별로 문제 풀이를 분류하며, 하위 경로는 난이도와 문제 번호를 기준으로 구성합니다.
- 문제별 디렉터리에 소스 코드와 필요한 풀이 문서를 저장합니다.

## Getting Started

### 1. Repository Access

본 저장소는 GitHub Collaborator 권한을 기반으로 공동 관리합니다.
모든 문제 풀이는 각자의 GitHub 사용자명 디렉터리에 저장합니다.

- Main Repository: sonyeseul63/ALGO_STUDY

### 2. Automatic Upload

| Platform | Extension | Directory |
| --- | --- | --- |
| [Baekjoon](https://www.acmicpc.net/) | [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub) | `BOJ/` |
| [Programmers](https://school.programmers.co.kr/) | [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub) | `PROG/` |
| [SWEA](https://swexpertacademy.com/main/main.do) | [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub) | `SWEA/` |
| [LeetCode](https://leetcode.com/) | [LeetHub-Neo](https://github.com/legojeon/LeetHub-Neo) | `LeetCode/` |

#### BaekjoonHub

확장 프로그램에서 GitHub 저장소를 연결한 뒤 **Directory Path Template**을 설정합니다.

`<GITHUB_ID>`를 자신의 GitHub 사용자명으로 변경합니다.

| Platform | Directory Path Template |
| --- | --- |
| Baekjoon | `<GITHUB_ID>/BOJ/${level}/${id}. ${title}` |
| Programmers | `<GITHUB_ID>/PROG/${level}/${id}. ${title}` |
| SWEA | `<GITHUB_ID>/SWEA/${level}/${id}. ${title}` |

설정 저장 후 정답을 제출하여 생성된 GitHub 경로를 확인합니다. SWEA는 업로드 버튼을 통한 수동 동기화가 필요할 수도 있습니다.

#### LeetHub-Neo

GitHub 저장소 연결 후 **Sync Folder**를 다음과 같이 설정합니다.

```text
<GITHUB_ID>/LeetCode
```

공유 저장소의 최상위 README가 변경되지 않도록 `Auto update root README` 옵션은 비활성화합니다.

### 3. Manual Upload

자동 업로드를 지원하지 않거나 로컬에서 직접 작성한 풀이도 자신의 디렉터리에 추가할 수 있습니다.

```text
<GITHUB_ID>/<PLATFORM>/<PROBLEM>/
```

수동 업로드 시 다른 팀원의 변경 사항을 먼저 동기화한 후 커밋합니다.

```bash
git pull --rebase origin main
git add .
git commit -m "docs: add solution notes"
git push origin main
```

## Repository Guidelines

- **Directory ownership:** 모든 문제 풀이는 자신의 GitHub 사용자명 디렉터리에 저장합니다.
- **Naming:** 자동 생성된 문제 번호 및 제목 기반 디렉터리 구조를 유지합니다.
- **Commit:** 자동 업로드의 커밋 메시지는 확장 프로그램 기본 형식을 따릅니다. 수동 커밋은 변경 내용을 명확하게 작성합니다.
- **Documentation:** 오답 분석, 접근 방식, 시간·공간 복잡도 등의 학습 기록은 필요에 따라 추가합니다.
- **Collaboration:** 공통 설정이나 최상위 README 변경은 다른 팀원에게 영향을 주지 않도록 사전에 확인합니다.

문제 풀이 업로드는 확장 프로그램에서 처리하며, 파일 이동을 위한 GitHub Actions는 사용하지 않습니다.
