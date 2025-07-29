## Youtube Video Downloader
Any videos including private, live, longer than 3hrs are supported.

1. Extract `cookies.txt` for login session by [Chrome extension](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc). Cookie should be in Netscape format, and extracted from the page with the video. Add in `cookies.txt`.
2. `pip install yt-dlp`
3. secure space for video
3 hours HD vid generally takes up 2-5GB
4. run.

It automatically selects the best resolution, extract video `.mp4` and audio `.webm` then merge into `.mkv` (`ffmpeg`) by `yt-dlp`.  
Resumes if interrupted by network stability or rate limits.
