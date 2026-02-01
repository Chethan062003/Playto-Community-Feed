# EXPLAINER

## 1. The Tree — Modeling Nested Comments

I modeled threaded comments using the **Adjacency List pattern**:

parent = ForeignKey('self', null=True, blank=True, related_name='replies')

This allows comments to reply to other comments with unlimited nesting depth, similar to Reddit-style discussions.

### Avoiding the N+1 Query Problem

A naive recursive serializer would hit the database once per reply, causing N+1 queries.

To prevent this, I fetch **all comments for a post in a single query** and build the tree in memory using a dictionary:

- Query all comments for the post
- Group them using `comment_map[parent_id]`
- Recursively serialize from this in-memory structure

This ensures that loading a post with 50 nested comments still uses **only one DB query** for comments.

---

## 2. The Math — 24 Hour Leaderboard

Karma is **not stored** on the User model.

Instead, it is dynamically calculated from the `Like` table using only activity from the last 24 hours.

Rules:

- 1 Like on a Post = 5 Karma
- 1 Like on a Comment = 1 Karma

### QuerySet used

```python
since = now() - timedelta(hours=24)

likes = Like.objects.filter(created_at__gte=since)

leaderboard = likes.annotate(
    karma=Case(
        When(post__isnull=False, then=5),
        When(comment__isnull=False, then=1),
        output_field=IntegerField()
    ),
    owner=Case(
        When(post__isnull=False, then=F('post__author')),
        When(comment__isnull=False, then=F('comment__author')),
    )
).values('owner').annotate(
    total_karma=Sum('karma')
).order_by('-total_karma')[:5]
