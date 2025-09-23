from enum import StrEnum


class RequestActions(StrEnum):
    OPENED = 'opened'
    REOPENED = 'reopened'
    CLOSED = 'closed'
    SYNCHRONIZE = 'synchronize'
    EDITED = 'edited'
    ASSIGNED = 'assigned'
    UNASSIGNED = 'unassigned'
    LABELED = 'labeled'
    UNLABELED = 'unlabeled'
    LOCKED = 'locked'
    UNLOCKED = 'unlocked'
    REVIEW_REQUESTED = 'review_requested'
    REVIEW_REQUEST_REMOVED = 'review_request_removed'
    READY_FOR_REVIEW = 'ready_for_review'
    CONVERTED_TO_DRAFT = 'converted_to_draft'
    SUBMITTED = 'submitted'
    DISMISSED = 'dismissed'
    CREATED = 'created'
    DELETED = 'deleted'


class ReviewState(StrEnum):
    APPROVED = 'approved'
    CHANGES_REQUESTED = 'changes_requested'
    COMMENTED = 'commented'
    DISMISSED = 'dismissed'
    PENDING = 'pending'


class WorkflowRunStatus(StrEnum):
    REQUESTED = 'requested'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    QUEUED = 'queued'
    PENDING = 'pending'
    WAITING = 'waiting'


class WorkflowRunConclusions(StrEnum):
    ACTION_REQUIRED = 'action_required'
    CANCELLED = 'cancelled'
    FAILURE = 'failure'
    NEUTRAL = 'neutral'
    SKIPPED = 'skipped'
    STALE = 'stale'
    SUCCESS = 'success'
    TIMED_OUT = 'timed_out'
    STARTUP_FAILURE = 'startup_failure'
