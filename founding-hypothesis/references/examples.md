# Founding Hypothesis — Worked Examples

## How to read these examples

- **Example 1 (Spotify at its start)** is a **retrospective reconstruction**. Spotify never published a Founding Hypothesis; this is what the hypothesis could have looked like in 2006-2008, before launch, built from public facts about the company. The sources are listed at the end, and each fact used is tied to one. Anything that isn't a sourced fact is marked **(assumption)**.
- **Example 2 (Gmail)** is the one example from the authors that could be verified in text. It's quoted briefly; the full hypothesis in the source is an image.
- **Example 3** contrasts a weak and a strong sentence for the same idea.
- Don't treat these as the "right answer". They show the *shape* and the *level of specificity* to aim for.

---

## Example 1 — Spotify (reconstruction, 2006-2008, before launch)

### Context (sourced facts)

- Spotify was founded in April 2006 in Stockholm by Daniel Ek and Martin Lorentzon, conceived as a legal alternative to piracy. [1]
- Ek has said he set out to "create a product that was better than piracy". [2] He reportedly argued to the labels that you beat piracy "by having a better product, not by trying to shut them down". [3]
- Ek had briefly been CEO of uTorrent (until its sale to BitTorrent in December 2006); Lorentzon had co-founded TradeDoubler, which acquired Ek's earlier company Advertigo. [4]
- Licensing music from the major labels took roughly two years of negotiation before the public launch. [1]
- Launch: October 2008, in Sweden and a few other European countries, initially by invitation only; US launch in 2011. [1][4]

### The basics (Day 1)

| Step | Answer |
|---|---|
| **Target customer** | Music lovers in Sweden, mid-2000s, who today get most of their music through file sharing (BitTorrent sites, Kazaa-style networks) and have a large personal library on their computer and player. *(assumption: they would switch if a legal option were as easy)* |
| **Important problem** | Getting the song you want means finding it, downloading it, and managing files, and doing it illegally carries risk and unease. The legal alternative at the time was mostly buying tracks one by one. *(assumption: this hassle plus the legal unease is painful enough to change behavior)* |
| **Our advantage** | Ek knows file sharing from the inside (ex-CEO of uTorrent) and Lorentzon knows online advertising (TradeDoubler), which points toward a free, ad-funded model. [4] One source also says uTorrent's creator, Ludvig Strigeus, joined Spotify. [4] |
| **Competitors / alternatives** | File sharing (BitTorrent sites, Kazaa-style networks) · pay-per-track download stores · CDs and the library already on the user's computer · radio · "do nothing: keep what I have". |
| **Most challenging competitor** | **File sharing.** It is free, its catalog is enormous, and it is already a habit. |

### Differentiation

| Differentiator | Relative to | Swap test ("could the competitor say it too?") |
|---|---|---|
| **As instant and unlimited as file sharing, but legal** | File sharing | File sharing can't say "legal". Download stores can't say "instant and unlimited". ✅ |
| **Free to start, with no files to download or manage** | Pay-per-track stores and file sharing | Stores charge per track; file sharing has the files-to-manage hassle. ✅ |

### Approach (Day 2): three genuinely different options

| Approach | Customer experience | Feasibility | Growth potential | Financial viability | Licensing *(custom lens)* |
|---|---|---|---|---|---|
| **A. A cheaper legal download store** | Low: still files to buy and manage, so it doesn't beat file sharing | High | Low: nobody switches from free to paid-per-track | Medium | Medium |
| **B. Streaming with instant playback, free with ads** *(top bet)* | High: feels like your own library, nothing to download | Low-Medium: playback has to start fast enough to feel local | High: free tier removes the barrier to try; friends can share songs | Low-Medium: ad revenue has to cover what is paid to the labels | **Low**: needs deals with the major labels |
| **C. Paid-only streaming, no free tier** *(backup)* | High | Low-Medium | Low: file-sharers won't pay up front for something they get free today | Medium: clearer revenue per user | **Low**: same dependency on label deals |

*Ratings are illustrative judgments, not measurements.* The custom "Licensing" lens is what makes this example realistic: both streaming options depend on label deals, and in reality those took about two years. [1]

**Top bet:** B. **Backup:** C, a paid ad-free subscription, if ad revenue can't cover royalties.

### The Founding Hypothesis

> If we help **music lovers in Sweden who today get their music through file sharing** solve **the hassle of finding, downloading and managing songs, and the unease of doing it illegally**, with **a streaming player that starts any song instantly and is free to use with ads** (backup: **a paid, ad-free subscription**), we believe they will choose it over **file sharing and pay-per-track download stores** because our solution is **as instant and unlimited as file sharing, but legal**, and **free to start, with no files to manage**.

### Assumption scorecard

| # | Belief | Why we believe it | What would prove us wrong | Risk | Next step |
|---|---|---|---|---|---|
| 1 | **Right customer:** Swedish file-sharers are the right people to start with | Assumption. Context: Ek comes from Sweden and ties his motivation to piracy. [2] | Interviewees who file-share but say they'd never move to any legal service, whatever it offers | Medium | Interview 10-15 people who file-share about how they get music today |
| 2 | **Right problem:** the hassle (and legal unease) is painful enough to change behavior | Assumption | Most interviewees say their current routine "works fine" and the legal side doesn't bother them | Medium | Same interviews; observe how they actually find and organize songs |
| 3 ⚠️ | **Right approach:** we can deliver instant streaming of a catalog big enough to compete | Assumption: Ek's team has file-sharing technology experience [4] | Label deals aren't signed, so the catalog is too small to feel "unlimited"; or playback starts noticeably slower than a local file | **High** (both the catalog and the speed must hold) | Technical spike on playback start time **and** early conversations with the labels (a buyer-style conversation) |
| 4 | **They'll choose us over file sharing:** file-sharers make it their main source | Assumption | After a few weeks, testers keep using file sharing as their main source | **High** | A small invite-only release; measure whether use of file sharing drops |
| 5 | **They care about our differentiators:** "legal" and "free" matter beyond "instant" | Assumption | Testers say only catalog completeness and speed matter and ignore the rest | Medium | Ask testers what made them stay or leave, and compare free vs. paid retention |

**Riskiest belief (⚠️): #3.** Without label licenses there's no "unlimited" catalog and the first differentiator collapses. This matches what the story shows: licensing consumed about two years before launch. [1]

> **Later evidence, not a Day-1 fact.** Spotify's own engineers published measurements of the shipped system in 2010: a median playback start time of 265 ms. [5] That shows the speed belief in #3 was achievable, but it was measured years after the hypothesis would have been written.

---

## Example 2 — Gmail (from the authors)

[Lenny's Newsletter](https://www.lennysnewsletter.com/p/introducing-the-foundation-sprint) reverse-engineers Gmail's original promise: *"We'll solve your overflowing inbox problems better than Outlook, Hotmail, and Yahoo,"* winning on storage and search. The reconstructed hypothesis itself is an image in the article, so only the promise is quoted here.

Mapped to the template's slots:

| Slot | Gmail |
|---|---|
| Customer | People with overflowing inboxes |
| Problem | Inboxes that fill up and are hard to search |
| Competitors | Outlook, Hotmail, Yahoo |
| Differentiators | More storage, better search |

Notice that the differentiators are *contrasts with named competitors*, which is what makes them testable.

---

## Example 3 — Weak vs. strong (same idea)

**Weak:**
> If we help **people** solve **listening to music** with **an app**, they will choose it over **other music apps** because our solution has **a better UX** and **more songs**.

What's wrong:
- *"People"* isn't a customer: you can't go find them this week.
- *"Listening to music"* isn't a painful problem; it's an activity.
- *"An app"* is not an approach.
- Competitors are only look-alikes: no file sharing, no owned library, no "do nothing".
- *"Better UX"* and *"more songs"* fail the swap test: any competitor can say them.

**Strong:** see the Spotify sentence in Example 1. Every slot is specific, the competitors include the real one (file sharing), and the differentiators only make sense against a named competitor.

---

## Sources

1. [Spotify, Wikipedia](https://en.wikipedia.org/wiki/Spotify) and [Spotify History: Founded 2006, Full Timeline](https://corpdigest.com/company/spotify/company-history): founding date, motive, launch date and invite-only, two years of label licensing. *(Wikipedia is a tertiary source; the licensing duration comes from the timeline site, a secondary source.)*
2. [Spotify Founder Daniel Ek Wanted to Create Something "Better than Piracy"](https://abcnews.go.com/blogs/technology/2012/12/spotify-founder-daniel-ek-wanted-to-create-something-better-than-piracy) (ABC News, 2012): the "better than piracy" quote.
3. [Daniel Ek: The Big, Hairy, Audacious Goal of Spotify](https://glasp.ai/youtube/sXbxzkDJOzo) (summary of a Stanford talk) and [Spotify co-founder talks music](https://stanforddaily.com/2012/05/17/spotify-co-founder-talks-music/) (Stanford Daily): Ek's reasoning about beating piracy with a better product. *(The "by having a better product" phrasing reached me through a secondary summary of a Skavlan interview, so treat the exact wording with caution.)*
4. [Daniel Ek, Wikipedia](https://en.wikipedia.org/wiki/Daniel_Ek) and [Daniel Ek, Music Business Worldwide](https://www.musicbusinessworldwide.com/people/daniel-ek/): uTorrent, TradeDoubler/Advertigo, Strigeus. *(The Strigeus claim comes from a single source.)*
5. Kreitz & Niemelä, [Spotify – Large Scale, Low Latency, P2P Music-on-Demand Streaming](https://www.csc.kth.se/~gkreitz/spotify-p2p10/spotify-p2p10.pdf) (IEEE P2P'10): 265 ms median playback start.
